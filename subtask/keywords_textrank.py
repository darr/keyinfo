#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : keywords_textrank.py
# Create date : 2019-08-05 16:14
# Modified date : 2019-08-05 16:43
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from collections import defaultdict
import jieba.posseg as pseg
from .textrank import textrank_graph

class TextRank:
    def __init__(self):
        self.candi_pos = ['n', 'v', 'a']
        self.span = 5

    def extract_keywords(self, text, num_keywords):
        g = textrank_graph()
        cm = defaultdict(int)
        word_list = [[word.word, word.flag] for word in pseg.cut(text)]
        for i, word in enumerate(word_list):
            if word[1][0] in self.candi_pos and len(word[0]) > 1:
                for j in range(i + 1, i + self.span):
                    if j >= len(word_list):
                        break
                    if word_list[j][1][0] not in self.candi_pos or len(word_list[j][0]) < 2:
                        continue
                    pair = tuple((word[0], word_list[j][0]))
                    cm[(pair)] +=  1

        for terms, w in cm.items():
            g.addEdge(terms[0], terms[1], w)
        nodes_rank = g.rank()
        nodes_rank = sorted(nodes_rank.items(), key=lambda asd:asd[1], reverse=True)

        return nodes_rank[:num_keywords]
