#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : abstract_textrank.py
# Create date : 2019-08-05 16:15
# Modified date : 2019-08-05 16:42
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import re
from collections import defaultdict
import jieba.posseg as pseg
from .textrank import textrank_graph
from .sentence_similarity import SimilarityCompute

class AbstarctTextrank:
    def __init__(self):
        self.span = 3
        self.similer = SimilarityCompute()
        self.sim_score = 0.5 #句子相似度阈值，用于构建句子之间的边

    def sentence_split(self, text):
        sentence_dict = {}
        sentences = [sentence for sentence in re.split(r'[？！。;；\n\r]', text) if sentence]
        for index, sentence in enumerate(sentences):
            sentence_dict[index] = [sentence, [word.word for word in pseg.cut(sentence) if word.flag[0] not in ['x', 'u', 'p', 'w']]]
        return sentence_dict

    def extract_abstract(self, text, num_sentences):
        sentence_dict = self.sentence_split(text)
        g = textrank_graph()
        cm = defaultdict(int)
        for i, s1 in sentence_dict.items():
            for j, s2 in sentence_dict.items():
                sim_score = self.similer.similarity_cosine(s1[1], s2[1])
                if sim_score >= 0.5:
                    cm[(s1[0], s2[0])] += 1
        for terms, w in cm.items():
            g.addEdge(terms[0], terms[1], w)
        nodes_rank = g.rank()
        nodes_rank = sorted(nodes_rank.items(), key=lambda asd: asd[1], reverse=True)
        return nodes_rank[:num_sentences]
