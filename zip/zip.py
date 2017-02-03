# coding=gbk

import ConfigParser
import os
import Tkinter
import tkFileDialog
import zlib
import zipfile

#遍历文件
def walkFiles(filePath):

    #目标文件路径
    #destDir = os.path.join(os.getcwd(), 'zip')
    destDir = targetDir

    #源文件目录
    pathDir = os.listdir(filePath)
    
    pathArr = []
    
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

            #将压缩的文件写入到新目录
            compress(child, destfile)

'''
根据选取的文件进行压缩
'''     
def zipFiles(filelist):

    destDir = targetDir

    pathArr = []
    for childfile in filelist:
        
        childfile = os.path.normpath(childfile)

        filename = os.path.basename(childfile)
        
        if(len(pathArr) == 0):
            pathArr = childfile.split(os.sep)
            print pathArr[-2]

        childDir = os.path.join(destDir, pathArr[-2])

        if not os.path.isdir(childDir):
            os.makedirs(childDir)

        destfile = os.path.join(childDir, filename)

        #将压缩的文件写入到新目录
        compress(childfile, destfile)
        

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

    #源文件路径
    sourceDir = "srcPath"
    #压缩后存放路径
    targetDir = "tarPath"
    
    #配置文件
    cfFile = "config_unzip.ini"

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

    inpu = raw_input("\n选择全部压缩 输入1，单独文件压缩输入 2: ")
    if(inpu == '1'):
        
        sourceDir = os.path.normpath(sourceDir)
        walkFiles(sourceDir)
        
    elif(inpu == '2'):
        print "选中的文件: "
        master = Tkinter.Tk()
        #master.withdraw() #不显示界面主窗口
        #master.mainloop()
        '''
        options = {}  
        options['defaultextension'] = '.bin'  
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]  
        options['initialdir'] = 'C:\\'  
        options['initialfile'] = 'myfile.txt'  
        options['parent'] = master
        options['title'] = '选取要压缩的文件'
        '''
        
        filenames = tkFileDialog.askopenfilenames()
        print '\n'.join(list(filenames))
        print "开始压缩"
        zipFiles(filenames)

        master.destroy()

    else:
        print "退出"
    
    raw_input("压缩完毕 按 回车键 退出")
    exit()
