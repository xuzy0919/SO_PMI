#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import jieba.posseg as pseg

try:
    conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306,
                           charset='utf8')
    cursor = conn.cursor()
    word_dict = {}
    sql1 = "SELECT * FROM result;"
    cursor.execute(sql1)
    result_list = cursor.fetchall()

    for row in result_list:
        id = row[0]
        sentence = row[2]
        word_list = pseg.cut(sentence)
        for elem in word_list:
            if elem.flag == "a":
                sql2 = "INSERT INTO word_information ( review_id, word ) VALUES ( %d, \"%s\" )" % (id, elem.word)
                try:
                    cursor.execute(sql2)
                    conn.commit()
                    print elem.word
                except:
                    conn.rollback()
except MySQLdb.Error, e:
    print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
