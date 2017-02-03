# coding=gbk

import ConfigParser
import os
import zlib
import zipfile

#遍历文件
def walkFiles(filePath):

    #解压后写入目录
    #destDir = os.path.join(os.getcwd(), 'test_unzip')
    destDir = targetDir

    #压缩文件源目录
    pathDir = os.listdir(filePath)

    pathArr = [];
    for alldir in pathDir:
        
        #源文件绝对路径
        child = os.path.join(filePath, alldir)
        
        #子目录
        if os.path.isdir(child):
            #print child
            walkFiles(child)
            
        else:
            if(len(pathArr) == 0):
                pathArr = filePath.split(os.sep)
                print pathArr[-1]
            
            childDir = os.path.join(destDir, pathArr[-1])
                
            if not os.path.isdir(childDir):
                os.makedirs(childDir)

            destfile = os.path.join(childDir, alldir)
            
            #print destfile

            #将解压的文件写入到新目录
            decompress(child, destfile)        
        

def compress(infile, dest, level=-1):
    infile = open(infile, 'rb')
    dest = open(dest, 'wb')
    com = zlib.compressobj(level)
    data = infile.read(1024)
    while data:
        dest.write(com.compress(data))
        data = infile.read(1024)
    dest.write(com.flush())
                               
def decompress(infile, dest):
    infile = open(infile, 'rb')
    dest = open(dest, 'wb')
    decom = zlib.decompressobj()
    data = infile.read(1024)
    while data:
        dest.write(decom.decompress(data))
        data = infile.read(1014)
    dest.write(decom.flush())
            

if __name__ == '__main__':

    #压缩文件源路径
    sourceDir = "srcPath"
    #解压后存放路径
    targetDir = "tarPath"
    
    #配置文件
    cfFile = "config.ini"

    #读取配置文件
    if(os.path.exists(cfFile)):
        cf = ConfigParser.ConfigParser()
        cf.read(cfFile)
        sourceDir = cf.get("main", "sourceDir")
        targetDir = cf.get("main", "targetDir")
    else:
        print "配置文件不存在！"
        raw_input("\n按 回车键 退出\n")
        exit()


    print "开始解压"
    sourceDir = os.path.normpath(sourceDir)
    walkFiles(sourceDir)
        

    raw_input("解压完毕 按 回车键 退出")
    exit()
