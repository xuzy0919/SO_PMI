#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
from Segment import devide

try:
    conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306,
                           charset='utf8')
    cursor = conn.cursor()
    word_dict = {}
    sql1 = "SELECT reviewContent FROM result;"
    cursor.execute(sql1)
    result_list = cursor.fetchall()

    for row in result_list:
        sentence = row[0]
        devide(sentence, word_dict)

    for key in word_dict:
        print key, word_dict[key]
        sql2 = "INSERT INTO word_list ( word, frequency ) VALUES ( \"%s\", %d );" % (key, word_dict[key])
        try:
            cursor.execute(sql2)
            conn.commit()
        except:
            conn.rollback()
    conn.close()

except MySQLdb.Error, e:
    print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
