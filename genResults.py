__author__ = 'amukhopadhyay'
from googleExcel import generateReport
from bs4 import BeautifulSoup
from mechanize import Browser
from mechanize import Browser
from datetime import datetime
import threading
from threading import Thread
from Queue import Queue
# from mechanize import

# var = raw_input("Please enter word: ")
# generateReport(var)
#

def actualCalling(q):
  while True:
    var = q.get()
    print var
    # print q.get()
    generateReport(var, wordDefn, wordSentence, wordDefnSentence, wordCovered)
    q.task_done()

path = "C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\wordsDontKnow.txt"
# wordSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordSentence.csv"
# wordDefn ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinition.csv"
# wordDefnSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinitionSentence.csv"
wordSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordSentence.csv"
wordDefn ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinition.csv"
wordDefnSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinitionSentence.csv"
# wordCovered="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordsAlreadyCovered.csv"
wordCovered="C:\\Users\\amukhopadhyay\\Desktop\\WordsAlreadyCovered.csv"
q = Queue(maxsize=0)
num_threads = 10
ins = open( path, "r" )
for line in ins:
    var = line.strip().replace("\n","")
    # print var, datetime.now().time()
    q.put(var)

for i in range(num_threads):
    worker = Thread(target=actualCalling, args=(q,))
    worker.setDaemon(True)
    worker.start()
q.join()












# # ______________________________________#
#
#
#
# __author__ = 'amukhopadhyay'
# from googleExcel import generateReport
# from bs4 import BeautifulSoup
# from mechanize import Browser
# from mechanize import Browser
# from datetime import datetime
# # from mechanize import
#
# # var = raw_input("Please enter word: ")
# # generateReport(var)
# #
#
# # path = "C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\wordsDontKnow.txt"
# # wordSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordSentence.csv"
# # wordDefn ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinition.csv"
# # wordDefnSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinitionSentence.csv"
# # wordCovered="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordsAlreadyCovered.csv"
#
# path = "C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\wordsDontKnow.txt"
# # wordSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordSentence.csv"
# # wordDefn ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinition.csv"
# # wordDefnSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinitionSentence.csv"
# wordSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordSentence.csv"
# wordDefn ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinition.csv"
# wordDefnSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinitionSentence.csv"
# # wordCovered="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordsAlreadyCovered.csv"
# wordCovered="C:\\Users\\amukhopadhyay\\Desktop\\WordsAlreadyCovered.csv"
#
# ins = open( path, "r" )
# for line in ins:
#     var = line.strip().replace("\n","")
#     print var, datetime.now().time()
#     generateReport(var, wordDefn, wordSentence, wordDefnSentence, wordCovered)