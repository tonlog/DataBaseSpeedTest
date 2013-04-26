__author__ = 'tonie'

import MySQLdb
import time
import re

def insert_data(data_set):
    conn = MySQLdb.connect(user="root", passwd="*",db="assignment",port=3306)
    conn.autocommit(False)
    cur = conn.cursor()
    print time.time()
    for i in range(400):
        Qr = "insert into test3 (col1,col2) values"
        for j in range(0,20000,2):
            Qr += "('%s', %s)," % (data_set[i*20000+j],data_set[i*20000+j+1])
        Qr = Qr[:len(Qr)-1]
        cur.execute(Qr)
    conn.commit()
    print time.time()
    cur.close()
    conn.close()

def readfile(file_name):
    mass_result_set = []
    file_reader = open(file_name,'r')
    mass_text = file_reader.read()
    #re_str_for_letter = r"\b([^\d\s]+?)\b"
    #re_str_for_digit  = r"\b([\d]+?)\b"
    regex = r"\b([\w]+?)\b"

    #pattern_forStr = re.compile(re_str_for_letter)
    #pattern_forDigit = re.compile(re_str_for_digit)
    p = re.compile(regex)
    #m_str = pattern_forStr.findall(mass_text)
    #m_digit = pattern_forDigit.findall(mass_text)
    m = p.findall(mass_text)

    '''
    if len(m_str) == len(m_digit):
        for i in range(len(m_str)):
            mass_result_set.append([m_str[i],m_digit[i]])
            '''
    for i in range(0,len(m)):
        mass_result_set.append(m[i])

    file_reader.close()
    return mass_result_set

if __name__=='__main__':
    print time.time()
    file_name = 'X:\\Desk\\test1.txt'
    data =  readfile(file_name)
    insert_data(data)