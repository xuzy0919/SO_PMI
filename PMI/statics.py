#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

try:
    conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    fre_t = 0

    # 候选词集
    sql1 = "SELECT word FROM candidate;"
    cursor.execute(sql1)
    candidateSet = cursor.fetchall()

    # 影评集
    sql2 = "SELECT reviewContent FROM result";
    cursor.execute(sql2)
    reviewSet = cursor.fetchall()

    # 种子词集
    sql3 = "SELECT word FROM seed_p;"
    cursor.execute(sql2)
    seedSet = cursor.fetchall()

    for row in candidateSet:
        candidate = row[0]
        print candidate + ":"
        for row in seedSet:
            fre_t = 0
            seed = row[0]
            for row in reviewSet:
                sentence = row[0]
                if sentence.count(seed) > 0 and sentence.count(candidate) > 0:
                    fre_t = fre_t + 1
                    str = candidate + seed
                    print str
                    print fre_t
            sql4 = "UPDATE pmi_p SET frequency_t = %d WHERE candidate = \"%s\" AND seed = \"%s\"" % (
            fre_t, candidate, seed)
            try:
                cursor.execute(sql4)
                conn.commit()
            except:
                conn.rollback()

except MySQLdb.Error, e:
    print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
