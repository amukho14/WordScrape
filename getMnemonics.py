__author__ = 'amukhopadhyay'


def returnMnemonics(var):
    from mechanize import Browser
    from bs4 import BeautifulSoup
    # var = "abase"
    br = Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    url= 'http://mnemonicdictionary.com/?word=' + str(var)
    br.open(url)

    soup_mn = BeautifulSoup(br.response().read())

    # <div style="padding-top: 10px;">
    count_mn=0
    mnemonics=""
    for i in soup_mn.find_all('div',{'style':'padding-top: 10px;'}):

        soup2 = BeautifulSoup(str(i))
        # buildDef = ""
        # print soup2.prettify()
        for x in soup2.find_all('div', {'class':'row-fluid'}):
            soup3 = BeautifulSoup(str(x))

            for y in soup3.find_all('div', {'class':'span9'}):
                count = 0
                # print count_mn
                if count_mn==3:
                    break
                count_mn = count_mn+1
                if y is not None:
                    for z in y:
                        if count == 2:
                            # print z
                            mnemonics = mnemonics+z.strip().replace(','," ").replace('\n', '').replace(".","")+","
                        count = count+1
    return mnemonics
#
# var = "incumbent"
# print returnMnemonics(var)