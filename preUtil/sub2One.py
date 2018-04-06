#coding:utf-8

import os
import sys
import re
import chardet
#这个脚本将递归地读取文件夹下的所有文件
#把一个句子写成一行
#把根目录和文件名区分开
#打印到根目录下,文件名+.txt的文件中

cn1 = '大学计算机基础'
cn2 = '大学物理'
cn3 = '高等数学一'
cn4 = '高等数学二'

cr1 = '816edeed-8b21-4ee0-92c1-addcccfb7933'
cr2 = 'fc18b458-f922-429b-a367-0fbf8bd31936'
cr3 = '0413c47e-e9e5-4a4e-9b36-ce8a28078cf0'
cr4 = '70bbcf03-9a64-45b6-bd5e-ae3d02302db7'


rootdir = "../data/smk/"
# dirList = os.listdir(rootdir)

def subMatch(sub):
    if re.match('\d*\Z',sub) or re.match('\d*\:\d*\:\d*.*', sub) or len(sub.strip()) < 1:
        return False
    return True

def convert(fname):#把一个文件中的内容变成一行字符串。注意是一行！！
    print('cvt:' + fname)
    infile = open(fname, 'rb')
    cStream = infile.read()
    encoding = chardet.detect(cStream)['encoding']
    if encoding == None:
        return ''
    sents = cStream.decode(encoding);
    infile.close()
    strs = []
    str = ""
    cnt = 0
    for line in sents.split('\n'):
        if cnt == 0:
            cnt += 1
            continue

        str = line.strip()
        if subMatch(str):
            cnt += 1
            if cnt < 5:
                print(str)
            strs.append(str + '\n')

    return strs

def convertMultiple(textFileDir, outName):#textFileDir: 传递目录名，outName：传递写的文件名

    fileDirList = os.listdir(textFileDir)

    for textFileOrDir in fileDirList:  # iterate through pdfs in pdf directory
        fileExtension = textFileOrDir.split(".")[-1]
        # txtName = rootdir + "/" + tempName + ".srt"
        tempDir = textFileDir + "/" + textFileOrDir

        if fileExtension == "srt":#这是一个字幕文件
            strs = convert(tempDir)  # get string of text content of textFile
            textFile = open(outName, "a")  # make text file
            # print(strs)
            for str in strs:
                textFile.write(str)  # write text to text file
                # print(str)
            textFile.flush()
            textFile.close()

        elif os.path.isdir(tempDir):#这是一个文件夹
            print("Entering Dir: " + tempDir)
            convertMultiple(tempDir, outName)

def main():

    # pdfDir = "" + rootdir
    # tempName = "noShow"# + unicode(txtDir, "UTF-8")
    #
    # convertMultiple(pdfDir, tempName)

    # print(subMatch('02'))
    # print(subMatch('00:00:09,519 --> 00:00:12,400'))
    # print(subMatch('00:00:0'))
    # print(subMatch('02号'))
    # print(subMatch('我就是想让它做2加7等于多少'))
    # print(subMatch('我'))
    # print(subMatch('我\n'))
    # print(subMatch('\n\n'))

    convertMultiple(rootdir + cr1, rootdir + cn1 + '.txt')
    convertMultiple(rootdir + cr2, rootdir + cn2 + '.txt')
    convertMultiple(rootdir + cr3, rootdir + cn3 + '.txt')
    convertMultiple(rootdir + cr4, rootdir + cn4 + '.txt')




if __name__ == "__main__":
    main()





