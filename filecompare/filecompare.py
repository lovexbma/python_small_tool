# coding=gbk
'''
copy from Internet
mod by xbma
'''
import os,ConfigParser

'''
递归列出某目录下的文件，放入List中
'''
def listDir (fileList,path):
    files=os.listdir(path)
    for i in  files:
        file_path = path + os.sep + i
        file_path = os.path.normpath(file_path)
        if os.path.isfile(file_path):
            fileList.append(file_path)
            
    for i in files:
        file_path = path + os.sep + i
        file_path = os.path.normpath(file_path)
        if os.path.isdir(file_path):
            listDir(fileList,file_path)
            
    return fileList

'''
将List中内容写入文件
'''
def writeListToFile(filelist, path):
    strs="\n".join(filelist)
    f=open(path,'wb')
    f.write(strs)
    f.close()
    
'''
读入文件内容并放入List中
'''
def readFileToList(path):
    lists=[]
    f=open(path,'rb')
    lines=f.readlines()
    for line in lines:
        lists.append(line.strip())
    f.close()
    return lists

'''
比较文件--以Set方式
'''
def compList(list1,list2):
    return list(set(list1)-set(list2))

'''
比较源路径文件和目标路径文件
将新增和修改的文件添加到列表中返回
'''
def compAllFiles(src, dest):
    allSrcFiles = []
    allSrcFiles = listDir(allSrcFiles, src)

    allDestFiles = []
    allDestFiles = listDir(allDestFiles, dest)

    diffList = []

    for srcfile in allSrcFiles:
        srcfilename = os.path.basename(srcfile)
        for destfile in allDestFiles:
            destfilename = os.path.basename(destfile)

            if(srcfilename == destfilename):
                if os.path.getsize(srcfile) != os.path.getsize(destfile):

                    diffList.append(srcfile)
                    
                    print srcfilename
            else:
                diffList.append(srcfile)

    return diffList

'''
复制List中文件到指定位置
'''
def copyFiles(fileList,targetDir):

    #分割路径
    pathArr = []
    #文件的根目录
    lastDir = ''
    
    for childfile in fileList:

        if(len(pathArr) == 0):
            pathArr = os.path.dirname(childfile).split(os.sep)
            lastDir = pathArr[-1]
            
        #目标路径
        targetPath=os.path.join(targetDir, lastDir)
        print targetPath
        #目标文件名 - 全路径
        targetFile=os.path.join(targetPath, os.path.basename(childfile))
        print targetFile

        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and os.path.getsize(targetFile)!=os.path.getsize(childfile)):
            print "正在复制文件：" + childfile
            open(targetFile,'wb').write(open(childfile,'rb').read())
        else:
            print "文件已存在，不复制！"
            
if __name__ == '__main__':
    path=".svn"
    #获取源目录
    txtFile="files.txt"
    #目录结构输出的目的文件
    tdir="cpfile"
    #复制到的目标目录
    cfFile="config.ini";
    #配置文件文件名
    fileList=[]
    #读取配置文件
    if(os.path.exists(cfFile)):
        cf=ConfigParser.ConfigParser()
        cf.read(cfFile)
        path=cf.get("main", "sourceDir")
        txtFile=cf.get("main","txtFile")
        tdir=cf.get("main","targetDir")
    else:
        print "配置文件不存在！"
        raw_input("\n按 回车键 退出\n")
        exit()

    print '开始对文件对比'
    resultArr = compAllFiles(path, tdir)
    if len(resultArr) > 0:
        print "有改多或者新增文件是: \n"
        print resultArr
        print "\n共计文件数：" + str(len(resultArr)) + "\n"

        if raw_input('\n是否复制文件？ (y/n)') != 'n':
            copyFiles(resultArr, tdir)
    else:
        print "没有不相同的文件"

    '''  
    if(os.path.exists(txtFile)):
        #如果导出的文件存在，就读取后比较
        list1=readFileToList(txtFile)
        print "正在读取文件列表……"
        fileList=listDir (fileList,path)
        print "正在比较文件……"
        list_res=compList(fileList,list1)
        if len(list_res)>0:
            print "以下是原目录中不存在的文件：\n"
            print "\n".join(list_res)
            print "\n共计文件数："+str(len(list_res))+"\n"
            if raw_input("\n是否复制文件？（y/n）") != 'n':
                copyFiles(list_res,tdir)
        else:
            print "没有不相同的文件！"
    else:
        #如果导出的文件不存在，则导出文件
        print "正在读取文件列表……"
        fileList=listDir (fileList,path)
        writeListToFile(fileList,txtFile)
        print "已保存到文件："+txtFile
    '''  
    raw_input("\n按 回车键 退出\n")
    exit()
