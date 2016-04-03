#!/usr/bin/python
# -*- coding: UTF-8 -*-
import jieba.posseg as pseg


def devide(str, dict):
    words = pseg.cut(str)
    # noun = ['n', 'nr', 'nz', 'nl', 'ng']
    for w in words:
        if w.flag == 'a':
            if w.word not in dict:
                dict[w.word] = 1
            else:
                dict[w.word] += 1
