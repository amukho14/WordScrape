__author__ = 'amukhopadhyay'

from googleExcel import generateReport
from bs4 import BeautifulSoup
from mechanize import Browser
from datetime import datetime

from getMnemonics import returnMnemonics


from random import shuffle
from threading import Thread
from Queue import Queue
import threading

#export to file with the followign conditions
#1) b/w each terms --> ";;;"
#2) b/w each term and def --> "---"
#3) So this will read, check for unique ones ONLY, and then shuffle and get mnemonics.

def getOnlyUniqueWords():
    path = "C:\\Users\\amukhopadhyay\\Desktop\\starQL.txt"
    # content=""
    uniqueContent=""
    with open(path,'r') as f:
        content = f.read()
    # print content

    #copy and replace the spl char (?) with ";;;"

    allWords = content.split(";;;")
    print len(allWords)

    for x in allWords:
        # print (i.split("---"))[0].replace(";","").capitalize()+"\\\\"
        i = (x.split(" ",1))
        if uniqueContent.__contains__(i[0]) == False:
            uniqueContent = uniqueContent+i[0].capitalize()+";;;"+i[1]+"//"
    # print uniqueContent

    x = [[i] for i in uniqueContent.split("//")]
    shuffle(x)
    return x

def actualWriting(q, writePath):
  while True:
    i = q.get()

    MY_LOCK.acquire()
    with open(writePath, 'a') as f:
        f.write("".join(i)+"//")
        f.close()
    MY_LOCK.release()
    q.task_done()

def addToQueue(x):
    for i in x:
        if i is not None:
            q.put(i)

def writeToFile(x, writePath):
    addToQueue(x)

    for i in range(num_threads):
        worker = Thread(target=actualWriting, args=(q,writePath))
        worker.setDaemon(True)
        worker.start()
    q.join()




listOfUniqueWords = getOnlyUniqueWords()
writePath = writePath="C:\\Users\\amukhopadhyay\\Desktop\\starBron.txt"
q = Queue(maxsize=0)
num_threads = 25
MY_LOCK = threading.Lock()

writeToFile(listOfUniqueWords, writePath)
#
