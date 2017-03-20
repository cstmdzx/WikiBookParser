# -*- coding:UTF-8 -*-
import urllib
import urllib2
import Queue
import os
import sys
import time
from HerfParser import href_parser
from HtmlToLine import html_to_line

# url = 'https://www.baidu.com'
# url = 'https://www.google.com/'
# url = 'https://en.wikipedia.org/wiki/Main_Page'
# url = 'http://baike.baidu.com/item/%E6%89%8B%E5%A5%97/1690692'
# url = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
# url = 'http://www.bbc.com/'
# url = 'http://sucre.blog.51cto.com/1084905/270556'
# url = 'https://zh.wikipedia.org/wiki/%E5%A4%A7%E8%A5%BF%E6%B4%8B%E9%A2%B6%E9%A2%A8%E5%AD%A3'
# url = 'http://baike.baidu.com/item/%E7%BD%91%E7%BA%A6%E8%BD%A6'

# set proxy, failed , maybe
#proxy = {'http':'192.168.190.201:1080'}
#proxy_support = urllib2.ProxyHandler(proxy)
#opener = urllib2.build_opener(proxy_support)
#urllib2.install_opener(opener)


# def download_html(url, url_header):
def download_html(url):
    # request = urllib2.Request(url, headers = url_header)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()


if __name__ == '__main__':
    '''
    dictRequestHead = {
    # 'Host':'zh.wikipedia.org',
    'Host':'zh.wikipedia.org',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'Cookie':'TBLkisOn=0; WMF-Last-Access=22-Dec-2016; CP=H2; GeoIP=US:DE:Wilmington:39.75:-75.55:v4; zhwikimwuser-sessionId=0b5c9cf6fdc94e8d',
    'Cache-Control':'max-age=0',
    'Referer':'None'}
    '''
    urlRoot = '/wiki/Category:%E5%8C%96%E5%AD%A6'
    # urlRoot = '/wiki/Category:Chemistry'
    urlWikiHome = 'https://zh.wikipedia.org'
    # urlWikiHome = 'https://en.wikipedia.org'
    # print urlRoot

    # test
    queueCategory = Queue.Queue(maxsize = 0) # infinite
    fileUrlPath = open('path', 'w')
    fileDownloadError = open('DownloadError', 'w')
    fileWriteError = open('WriteError', 'w')
    setVisitedUrl = set()
    queueCategory.put(urlRoot)
    pathStorage = './storage/'
    intMaxSize = 10000
    intCount = 0
    if not os.path.exists(pathStorage):
        os.mkdir(pathStorage)
    while( intCount < intMaxSize and not queueCategory.empty() ):
        url = queueCategory.get()
        page = download_html(urlWikiHome + url)
        '''
        for eachline in page:
            print eachline
        print page
        '''
        # print page.__len__()
        linePage = html_to_line(page)

        # fileTest.write(linePage)

        [listCategory, listPage] = href_parser(linePage)

        for eachPage in listPage:
            if eachPage[0] in setVisitedUrl:
                continue
            else:
                setVisitedUrl.add(eachPage[0])  # add to visited
                print str(time.time()) + ':' + urlWikiHome + eachPage[0]

                try:
                    strPage = download_html(urlWikiHome + eachPage[0])
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    print e
                    fileDownloadError.write(urlWikiHome + eachPage[0] + '\n')
                    fileDownloadError.write(str(e) + '\n')
                    continue
                fileUrlPath.write(url + '\t' + eachPage[0] + '\n')

                try:
                    fileTemp = open(pathStorage + eachPage[0][6:], 'w')
                    fileTemp.write(strPage)
                    intCount += 1
                    fileTemp.close()
                    print (intCount)
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    print e
                    fileWriteError.write(eachPage[0][6:] + '\n')
                    fileWriteError.write(str(e) + '\n')
                    continue


        for eachCategory in listCategory:
            if eachCategory[0] in setVisitedUrl:
                continue
            else:
                print str(time.time()) + ':' + urlWikiHome + eachCategory[0]
                queueCategory.put(eachCategory[0])  # add to visited
                fileUrlPath.write(url + '\t' + eachCategory[0] + '\n')

    fileUrlPath.close()
    fileDownloadError.close()
    fileWriteError.close()

