__author__ = 'amukhopadhyay'
__author__ = 'amukhopadhyay'

from googleExcel import generateReport
from bs4 import BeautifulSoup
from mechanize import Browser
from datetime import datetime

from threading import Thread
from Queue import Queue

from getMnemonics import returnMnemonics
from random import randint
import threading

from random import shuffle

MY_LOCK = threading.Lock()

def actualCalling(q):
  while True:
    i = q.get()
    var = "".join(i).split("---")
    print var[0]
    finalString = "".join(var[0])+"---"+"".join(var[1])+"\n"+returnMnemonics(var[0]).encode('utf-8')+ "\\\\"
    # print q.get()
    MY_LOCK.acquire()
    with open("C:\\Users\\amukhopadhyay\\Desktop\\"+str(randint(0,5))+".txt", 'a') as f:
        f.write(finalString)
        f.close()
        # f.write("".join(var)+"\n"+returnMnemonics(var[0]).encode('utf-8')+ "\\\\")
    MY_LOCK.release()
    q.task_done()


#export to file with the followign conditions
#1) b/w each terms --> ";;;"
#2) b/w each term and def --> "---"
#3) So this will read, check for unique ones ONLY, and then shuffle and get mnemonics.

def getOnlyUniqueWords(q):
    path = "C:\\Users\\amukhopadhyay\\Desktop\\BronGreyArea.txt"
    # content=""
    uniqueContent=""
    with open(path,'r') as f:
        content = f.read()
    allWords = content.split(";;;")
    # print allWords
    for i in allWords:
        i = i.strip().replace("%", "")
        if uniqueContent.__contains__(i) == False:
            uniqueContent = uniqueContent+i+"//"
    x = [[i] for i in uniqueContent.split("//")]
    shuffle(x)
    #MULTI THREAD THIS ENTIRE THING MAN. SPLIT INTO LIKE 6 PARTS AND MULTITHREAD IT.
    writePath="C:\\Users\\amukhopadhyay\\Desktop\\"
    j=0
    for i in x:
        if i is not None:
            q.put(i)
            # print ("".join(i).split("---"))[0], j
            # j+=1
            # val = "".join(i).split("---")
            # # print val[0], returnMnemonics(val[0])
            # j+=1
            # # if j%20 == 0:
            # print j
            # with open(writePath+"Dict"+str(j/600)+".txt", 'a') as f2:
            #         f2.write("".join(i)+"\n"+returnMnemonics(val[0]).encode('utf-8')+ "\\\\")

    # print "putting in QUEUE FINISHED"
q = Queue(maxsize=0)
num_threads = 20

getOnlyUniqueWords(q)

for i in range(num_threads):
    worker = Thread(target=actualCalling, args=(q,))
    worker.setDaemon(True)
    worker.start()
q.join()


#

