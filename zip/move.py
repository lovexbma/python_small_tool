# -*- coding: utf-8 -*-
import os
import shutil


#获取源目录下的所有文件名
allSrcFiles = []

#获取目标目录下的所有文件名
allDestFiles = []

'''
遍历文件目录
'''
def walkFiles(filePath, filetype):

    parentDir = os.listdir(filePath)
    
    for childDir in parentDir:

        childPath = os.path.join(filePath, childDir)

        if os.path.isdir(childPath):

            #递归
            walkFiles(childPath, filetype)
        else:
            if filetype is 1:
                allSrcFiles.append(childPath)
            else:
                allDestFiles.append(childPath)


def moveFiles():
    for inFile in allSrcFiles:
        inFileName = os.path.basename(inFile)

        for toFile in allDestFiles:
            toFileName = os.path.basename(toFile)
            print toFileName
            if os.path.walk
                print inFileName
            

if __name__=='__main__':
    srcDir = 'D:/PythonTestCode/zip/zip'
    destDir = 'D:/PythonTestCode/zip/event'

    walkFiles(srcDir, 1)
    walkFiles(destDir, 2)

    moveFiles()
