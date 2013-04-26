__author__ = 'njusoftware'

import re, MySQLdb,time
conn = MySQLdb.connect(user="root",passwd="*",db="assignment",port=3306)

file_reader = open("X:\\Desk\\test2.txt")
mass_text = file_reader.read()

regex = r"\b([^\d\s]+?)\b[\s]+?\b([\d]{1,3})\b[\s]+?\b([\w])\b"
p = re.compile(regex)
m = p.findall(mass_text)

cur = conn.cursor()
conn.autocommit(False)
sql_query = "insert into test2 (col1, col2, col3) values "

for i in range(len(m)):
    sql_query += "('%s', %s, '%s')," % tuple(m[i])
sql_query = sql_query[:len(sql_query)-1]

print time.time()
cur.execute(sql_query)
conn.commit()
print time.time()

cur.close()
conn.close()