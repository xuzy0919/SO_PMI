#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb, math

try:
    conn = MySQLdb.connect(host="111.186.113.134", user="root", passwd="root", db="filmreview", port=3306,
                           charset='utf8')
    cursor = conn.cursor()
    N = 547246
    sql1 = "SELECT * FROM pmi_n;"
    cursor.execute(sql1)
    resultSet = cursor.fetchall()
    for row in resultSet:
        id = row[0]
        fre_c = row[3]
        fre_s = row[4]
        fre_t = row[5]

        if fre_t != 0:
            pmi = math.log10(float(N * fre_t) / float(fre_c * fre_s))
            sql2 = "UPDATE pmi_n SET pmi_n = %f WHERE id = %d;" % (pmi, id)
            try:
                cursor.execute(sql2)
                conn.commit()
                print id
                print pmi
            except:
                conn.rollback()
        else:
            sql2 = "UPDATE pmi_n SET pmi_n = 0 WHERE id = %d;" % (id)
            try:
                cursor.execute(sql2)
                conn.commit()
            except:
                conn.rollback()
except MySQLdb.Error, e:
    print("MySQL Error %d: %s" % (e.args[0], e.args[1]))
