# -*- coding:UTF-8 -*-
import re

patternCategory = re.compile(r'<a class=\"CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory\" href=\"(.+?)\">(.+?)</a>')

patternPage = re.compile(r'<li><a href=\"(.+?)\" title=\".+?\">(.+?)</a></li>')

# filetest = open('testres', 'w')

def href_parser(html):
    # to parse link from html string
    # html is a str contains html from wiki
    # list_category contains the category's link and the txt
    # list_page contains the page's link, title and the txt
    list_category = patternCategory.findall(html)
    # filetest.write(html)
    # filetest.close()
    # 0.url  1.txt
    # count = 0
    '''
    for eachres in list_category:
        if eachres[0] == '':
            continue
        # print eachres[0]
        count += 1
        print eachres[1]
        print eachres[2]
        filetest.write('======================================================\n')
        filetest.write(eachres[1] + '\n')
        filetest.write('++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        filetest.write(eachres[2] + '\n')
    '''
    list_page = patternPage.findall(html)
    # 0.url  1.txt
    list_page.pop() # the last one is unuseful
    '''
    for each_ul in list_page:
        print each_ul[0]
        print each_ul[1]
    print list_category.__len__()
    print list_page.__len__()
    print count
    '''
    # list_href.extend(res[:][0])
    # print list_page
    return [list_category, list_page]

if __name__ == '__main__':
    fileHtml = open('RootUrl', 'r')
    lineHtml = fileHtml.readline()
    [listCategory, listPage] = href_parser(lineHtml)
    print listCategory.__len__()
    print listPage.__len__()
    print listCategory
    print listPage
    #print listHref


