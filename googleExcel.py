__author__ = 'amukhopadhyay'

from mechanize import Browser
from bs4 import BeautifulSoup
from getMnemonics import returnMnemonics
import threading
import os

# var = raw_input("Please enter word: ")
MY_LOCK = threading.Lock()
def generateReport(var, wordDefn, wordSentence,wordDefnSentence, wordCovered):

    if os.path.isfile(wordCovered) and var in open(wordCovered).read():
            print var, " is already covered"
            return
    mnemonics = returnMnemonics(var)
    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    url= 'http://www.oxforddictionaries.com/definition/english/' + str(var)
    # url= 'https://www.google.co.in/search?q=define+utilitarian'
    try:
        br.open(url)
    except:
        print "what word is this, man? " + var
        return
    soup = BeautifulSoup(br.response().read())
    # print soup.prettify()

    # data = open(url,'r').read()
    # soup=BeautifulSoup(data)
    # print soup.t

    # MY_LOCK.acquire()
    # with open(wordSentence, 'a') as f:
    #     # print var
    #
    #     f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", ")
    #     # f.write("\n")
    #     f.close()
    # with open(wordDefn, 'a') as f:
    #     # print var
    #     f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", ")
    #     # f.write("\n")
    #     f.close()
    # with open(wordDefnSentence, 'a') as f:
    #     # print var
    #     f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", ")
    #     # f.write("\n")
    #     f.close()
    # MY_LOCK.release()

    #get Defn

    definition=""
    for i in soup.find_all('span',{'class':'definition'}):
        soup2 = BeautifulSoup(str(i))
        for x in soup2.body:
            buildDef = ""
            if x is not None:
                for y in x:
                    if y.string is not None:
                        buildDef = buildDef + y.string.replace(',','')
            definition = definition + buildDef + ","
            # print definition


    # for Example Sentences
    sentence=""
    for i in soup.find_all('ul',{'class':'sentence_dictionary'}):
        if i is not None:
            soup2 = BeautifulSoup(str(i))
            for j in soup2.find_all('li',{'class':'sentence'}):
                if j is not None:
                    sentence = sentence + j.string.replace(',',' ').strip()+","
    # print sentence


    MY_LOCK.acquire()
    with open(wordSentence, 'a') as f:
        # print var

        f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", "+sentence.encode('utf-8')+"\n")
        # f.write("\n")
        f.close()
    with open(wordDefn, 'a') as f:
        # print var
        f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", "+definition.encode('utf-8')+"\n")
        # f.write("\n")
        f.close()
    with open(wordDefnSentence, 'a') as f:
        # print var
        f.write(var.encode('utf-8')+", "+mnemonics.encode('utf-8')+", "+definition.encode('utf-8')+", "+ sentence.encode('utf-8')+"\n")
        # f.write("\n")
        f.close()
    with open(wordCovered, 'a') as f:
        f.write(var.encode('utf-8')+",")
        f.close()
    MY_LOCK.release()

    return
