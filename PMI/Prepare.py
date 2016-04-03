#!/usr/bin/python
# -*- coding: UTF-8 -*-



import MySQLdb

try:
    conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306,
                           charset='utf8')
    cursor = conn.cursor()
    # 候选词集
    sql1 = "SELECT * FROM candidate;"
    cursor.execute(sql1)
    candidateSet = cursor.fetchall()

    # 种子词集
    sql3 = "SELECT * FROM seed_p;"
    cursor.execute(sql3)
    seedSet = cursor.fetchall()

    for row in candidateSet:
        candidate = row[1]
        can_fre = row[2]
        for row in seedSet:
            seed = row[1]
            seed_fre = row[2]
            sql4 = "INSERT INTO pmi_p ( candidate, seed, frequency_c, frequency_s, frequency_t ) VALUES ( \"%s\", \"%s\", %d, %d, 0 );" % (
                candidate, seed, can_fre, seed_fre)
            try:
                cursor.execute(sql4)
                conn.commit()
                print candidate + "+" + seed
            except:
                conn.rollback()

except MySQLdb.Error, e:
    print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
