__author__ = 'amukhopadhyay'
from googleExcel import generateReport
from bs4 import BeautifulSoup
from mechanize import Browser
# from mechanize import

# var = raw_input("Please enter word: ")
# generateReport(var)
#

path = "C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\wordsDontKnow.txt"
wordSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordSentence.csv"
wordDefn ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinition.csv"
wordDefnSentence ="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordDefinitionSentence.csv"
wordCovered="C:\\Users\\amukhopadhyay\\Downloads\\TrickyStuff\\PythonGrey\\WordsAlreadyCovered.csv"
ins = open( path, "r" )
for line in ins:
    var = line.strip().replace("\n","")
    # print var
    generateReport(var, wordDefn, wordSentence, wordDefnSentence, wordCovered)