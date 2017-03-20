# modify html to one line
# just for test

def html_to_line(page):
    str_line = ''
    for eachline in page:
        eachline = eachline.replace('\n', '')
        eachline = eachline.replace('\r', '')
        str_line += eachline
    return str_line


if __name__ == '__main__':
    fileTest = open('test.html', 'r')
    linesTest = fileTest.readlines()
    strHtml = html_to_line(linesTest)
    '''
    strHtml = ''
    for eachLineTest in linesTest:
        eachLineTest = eachLineTest.replace('\n', '')
        eachLineTest = eachLineTest.replace('\r', '')
        strHtml += eachLineTest
    '''
    fileRes = open('RootUrl', 'w')
    # strHtml = strHtml.replace('\n', '')
    # strHtml = strHtml.replace('\r', '')
    # strHtml.rstrip('')
    print strHtml
    fileRes.write(strHtml)


