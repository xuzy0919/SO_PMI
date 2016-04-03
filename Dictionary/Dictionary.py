#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306, charset='utf8')
cursor = conn.cursor()

sql1 = "SELECT word FROM swt_p;"

cursor.execute(sql1)
resultSet = cursor.fetchall()

for row in resultSet:
    word = row[0]
    # 在词频集里查找词典单词的词频
    sql2 = "SELECT frequency FROM wordlist WHERE word = '%s';" % (word)
    cursor.execute(sql2)
    result = cursor.fetchone()

    # 有匹配单词,更新swt_p或swt_n
    if result:
        frequency = result[0]
        print frequency
        sql3 = "UPDATE swt_p SET frequency = %d WHERE word = \"%s\"" % (frequency, word)
        try:
            cursor.execute(sql3)
            conn.commit()
        except:
            conn.rollback()

conn.close()
