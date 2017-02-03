# -*- coding: utf-8 -*-
import hashlib

arr = ["d9zk1dfachar_c_10120","d9zk1dfachar_c_10121",
        "d9zk1dfachar_c_10122","d9zk1dfachar_c_10123",
        "d9zk1dfachar_c_10124","d9zk1dfachar_c_10125",
        "d9zk1dfachar_c_10127","d9zk1dfachar_c_10128",
        "d9zk1dfachar_c_10129", "d9zk1dfachar_c_10131"]

def md5hex(word):  
    """ MD5加密算法，返回32位小写16进制符号 """  
    if isinstance(word, unicode):  
        word = word.encode("utf-8")  
    elif not isinstance(word, str):  
        word = str(word)  
    m = hashlib.md5()  
    m.update(word)  
    return m.hexdigest() 

for v in arr:
    """遍历数组生成md5码"""
    md5hash = md5hex(v)
    print md5hash