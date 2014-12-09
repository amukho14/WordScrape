__author__ = 'amukhopadhyay'

from googleExcel import generateReport
from bs4 import BeautifulSoup
from mechanize import Browser
from datetime import datetime


path = "C:\\Users\\amukhopadhyay\\Desktop\\star800.txt"
# path = "C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\wordsDontKnow.txt"
wordSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordSentence.csv"
wordDefn ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinition.csv"
wordDefnSentence ="C:\\Users\\amukhopadhyay\\Desktop\\WordDefinitionSentence.csv"
wordCovered="C:\\Users\\amukhopadhyay\\Desktop\\WordsAlreadyCovered.csv"
ins = open( path, "r" )

# generateReport("adjunct", wordDefn, wordSentence, wordDefnSentence)

for line in ins:
    var = line.strip().replace("\n","").split(" ")[0]
    print var, datetime.now().time()
    generateReport(var, wordDefn, wordSentence, wordDefnSentence, wordCovered)
