# -*- coding: utf-8 -*-
import hashlib
import os
import shutil

arrnum = ["10120","10121","10122","10123","10124",
          "10125","10127","10128","10129","10131"]


keywords_C = ["d9zk1dfachar_c_%s", "d9zk1dfachar_p_%s_02","d9zk1dfachar_p_%s_01",
            "d9zk1dfachar_p_%s_00","d9zk1dfachar_b_%s_02","d9zk1dfachar_b_%s_01",
            "d9zk1dfachar_b_%s_00"]

keywords_I = ["d9zk1dfachar_bt_%s_02", "d9zk1dfachar_bt_%s_01",
               "d9zk1dfachar_bt_%s_00", "d9zk1dfachar_bar_%s_02",
               "d9zk1dfachar_bar_%s_01", "d9zk1dfachar_bar_%s_00",
               "d9zk1dfachar_%s_02","d9zk1dfachar_%s_01","d9zk1dfachar_%s_00"] 

md5list = []

#缓存查找文件的md5码 C 文件夹下
md5dic_C = dict()

#缓存查找文件的md5码 I 文件夹下
md5dic_I = dict()

destDirC = "E:\\ShootGirlClient_Japan\\NewPicG\\%s\\c\\"
destDirI = "E:\\ShootGirlClient_Japan\\NewPicG\\%s\\i"

#using_id = "10131"

def md5hex(num_id):  
    """ MD5加密算法，返回32位小写16进制符号 """
    tempId_c = 0
    for keywordC in keywords_C:
        """ 获取 C 文件夹下的所有加密 """
        word = keywordC % num_id
        if isinstance(word, unicode):  
            word = word.encode("utf-8")  
        elif not isinstance(word, str):  
            word = str(word)  
        m = hashlib.md5()  
        m.update(word)
        
        tempId_c += 1
        strId = str(tempId_c)
        
        md5dic_C[num_id + strId] = m.hexdigest()

    tempId_i = 0
    for keywordI in keywords_I:
        """ 获取 I 文件夹下的所有加密 """
        word = keywordI % num_id
        if isinstance(word, unicode):  
            word = word.encode("utf-8")  
        elif not isinstance(word, str):  
            word = str(word)  
        m = hashlib.md5()  
        m.update(word)
        
        tempId_i += 1
        strId = str(tempId_i)
        
        md5dic_I[num_id + strId] = m.hexdigest()

def buildmd5():
    #md5hex(using_id)
    for v in arrnum:
        """遍历数组生成md5码"""
        md5hash = md5hex(v)

    for vc in md5dic_C:
        print "dic_C[%s] = " %vc, md5dic_C[vc]

    for vi in md5dic_I:
        print "dic_I[%s] = " %vi, md5dic_I[vi]

#遍历指定目录显示目录下的所有文件名
def walkFileC(filePath):
    pathDir = os.listdir(filePath)
    for allDir in pathDir:
        #child = os.path.join('%s%s' % (filePath, allDir))
        for key in md5dic_C:
            if allDir.find(md5dic_C[key]) != -1:
                newKey = key[0:len(key) - 1]
                child = os.path.join('%s%s' % (filePath, allDir))
                destDirK = os.path.join(destDirC % newKey)
                copyFile(child, destDirK)
                #print allDir

def walkFileI(filePath):
    pathDir = os.listdir(filePath)
    for allDir in pathDir:
        #child = os.path.join('%s%s' % (filePath, allDir))
        for key in md5dic_I:
            if allDir.find(md5dic_I[key]) != -1:
                newKey = key[0:len(key) - 1]
                child = os.path.join('%s%s' % (filePath, allDir))
                destDirK = os.path.join(destDirI % newKey)
                copyFile(child, destDirK)
                #print allDir
        
def copyFile(srcPath, destDir):
    fileName = os.path.basename(srcPath)
    destPath = destDir + "\\" + fileName
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        if not os.path.isdir(destDir):
            os.makedirs(destDir)
        print 'copy %s to %s' % (srcPath, destPath)
        shutil.copy(srcPath, destPath)
        
if __name__ == '__main__':
    filePathC = "E:\\ShootGirlClient_Japan\\sg_client\\ShootingGirl\\src\\c\\"
    filePathI = "E:\\ShootGirlClient_Japan\\sg_client\\ShootingGirl\\src\\i\\"

    buildmd5()
    
    walkFileC(filePathC)
    walkFileI(filePathI)
    



