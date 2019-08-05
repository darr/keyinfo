#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : keywords_tfidf.py
# Create date : 2019-08-05 16:14
# Modified date : 2019-08-05 16:44
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import jieba.posseg as pseg

class TFIDF:
    def __init__(self):
        self.idf_file = 'data/idf.txt'
        self.idf_dict, self.common_idf = self.load_idf()

    def build_wordsdict(self, text):
        word_dict = {}
        candi_words = []
        candi_dict = {}
        for word in pseg.cut(text):
            if word.flag[0] in ['n', 'v', 'a'] and len(word.word) > 1:
                candi_words.append(word.word)
            if word.word not in word_dict:
                word_dict[word.word] = 1
            else:
                word_dict[word.word] += 1
        count_total = sum(word_dict.values())
        for word, word_count in word_dict.items():
            if word in candi_words:
                candi_dict[word] = word_count/count_total
            else:
                continue

        return candi_dict

    def extract_keywords(self, text, num_keywords):
        keywords_dict = {}
        candi_dict = self.build_wordsdict(text)
        for word, word_tf in candi_dict.items():
            word_idf = self.idf_dict.get(word, self.common_idf)
            word_tfidf = word_idf * word_tf
            keywords_dict[word] = word_tfidf
        keywords_dict = sorted(keywords_dict.items(), key=lambda asd:asd[1], reverse=True)

        return keywords_dict[:num_keywords]

    def load_idf(self):
        idf_dict = {}
        for line in open(self.idf_file):
            word, freq = line.strip().split(' ')
            idf_dict[word] = float(freq)
        common_idf = sum(idf_dict.values())/len(idf_dict)

        return idf_dict, common_idf
