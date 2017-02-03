# -*- coding: cp936 -*-

import os
import re

def walkfiles(filepath):

    listdir = os.listdir(filepath)

    pathArr = []

    dirname = ''

    fileList = []
    
    for childdir in listdir:

        childfile = os.path.join(filepath, childdir)

        if os.path.isdir(childfile):
            
            walkfiles(childfile)
        else:

            if(len(pathArr) == 0):
                pathArr = filepath.split(os.sep)
                #print filepath
                #print pathArr[-1]

                dirname = pathArr[-1]
                
                dirList.append(dirname)
            
            filename = os.path.basename(childfile)

            if 'Dto' not in filename:

                #print filename

                fileList.append(filename)

                #文件全路径
                fullFileNameList.append(childfile)

        if len(fileList) > 0 and dirname != '':
            
            apiDic[dirname] = fileList
                

def readFromFile(filelist):

     #值字典 存放类名和对应的值列表
     valueDic = dict()
         
     for childfile in filelist:

         #返回文件路径名和文件名（带扩展）
         (filepath, tempfilename) = os.path.split(childfile)
         
         #返回文件名和扩展名
         #(shotname, extension) = os.path.splitext(tempfilename)

         #值列表 存放单个正则匹配出的 endurl parameters
         singleValueList = []
         
         f = open(childfile, 'rb')
         
         lines = f.readlines()

         for line in lines:
             tripline = line.strip()

             #匹配 endurl 名
             urlMatchObj = re.match(r'(.+)=(.+\/\w+\/\w+.*)', tripline, re.M|re.I)

             if urlMatchObj:
                 #print 'endUrl    --> : ', urlMatchObj.group(2)

                 singleValueList.append(urlMatchObj.group(2))

             #else:
                 #print "No match!"

             #匹配 参数 
             paraMatchObj = re.match(r'.+apiRequest\((.+)\).+', tripline, re.M|re.I)

             if paraMatchObj:
                 #print 'parameters --> : ', paraMatchObj.group(1)

                 singleValueList.append(paraMatchObj.group(1))
             #else:
                 #singleValueList.append('') #有的方法没有参数
             
         #存放类名和对应的值列表
         valueDic[tempfilename] = singleValueList

     return valueDic



def writeToFile(dic, path):

    f = open(path, 'wb')

    dirCount = 0
    fileCount = 0

    #字典排序 返回的是元组列表
    sortedTuple = sorted(apiDic.items(), key=lambda d:d[0])

    #childtuple[0] 是先前字典里的 key childtuple[1]是先前字典里的值
    for childtuple in sortedTuple:
        dirCount += 1
        
        dirname = childtuple[0] #目录名
        filelist = childtuple[1]#目录下的类名


        classInDirCount = len(filelist) #单目录下的类数量

        linename = '-----------%s---------- Count: %s ' % (dirname, classInDirCount)

        #apinames = "\r\n".join(filelist)

        fileCount += len(filelist)

        f.write(linename)
        
        f.write('\r\n')
        
        for apiclass in filelist:
            
            paralist = paramDic[apiclass] #类名对应的参数列表

            f.write(apiclass) #写入类名
            f.write('  --  ')
            
            if len(paralist) is 2:
                f.write("EndURL:" + paralist[0] + '\n')
                f.write("FuncPara:" + paralist[1])
            else:
                f.write("EndURL:" + paralist[0] + '\n')
                f.write("FuncPara:无参数")

            f.write('\r\n')
            
        f.write('\r\n')
        f.write('\r\n')

        print "Writing %s" % dirname
    

    lastStr = "Total Dir %s --- Total Files %s" % (dirCount, fileCount)
    f.write(lastStr)
    
    f.close()


def sortedDictValues(dic):
    items = dic.items()
    items.sort()

    return [value for key, value in items]

if __name__ == '__main__':

    #目录名 API cateory
    dirList = []

    #目录下的文件名 api name
    apiList = []

    #目录对应文件名  api cateory -- api names
    apiDic = dict()

    #排序后的字典
    sortedDic = dict()

    #文件全路径
    fullFileNameList = []

    #类名和对应的endurl para 属性
    paramDic = dict()

    #-----遍历文件夹下的所有类文件 找出 api 类
    filepath = 'D:/PythonTestCode/filefilter/api/'
    filepath = os.path.normpath(filepath)
    walkfiles(filepath)
    

    #------遍历读取上一步提取的 api 类，读取 endurl parameters
    paramDic = readFromFile(fullFileNameList)

    #for key in paramDic:
        #print "%s" %key, fileDic[key]


    
    #------将类所在的目录名 类名 类拥有的 endul paramters 参数写入
    writefile = 'D:/PythonTestCode/filefilter/api.txt'
    writeToFile(apiDic, writefile)

    #print '\n'.join(fullFileNameList)

    
