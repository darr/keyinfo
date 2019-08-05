#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : keyinfo.py
# Create date : 2019-08-05 16:39
# Modified date : 2019-08-05 16:41
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from subtask.keywords_textrank import TextRank
from subtask.keywords_tfidf import TFIDF
from subtask.abstract_textrank import AbstarctTextrank

class KeyInfoExtract:
    def __init__(self):
        self.kewords_textanker = TextRank()
        self.kewords_tfidfer = TFIDF()
        self.abstract_textranker = AbstarctTextrank()

    def extract_keywords_textrank(self, text, num_keywords):
        return self.kewords_textanker.extract_keywords(text, num_keywords)

    def extract_keywords_tfidf(self, text, num_keywords):
        return self.kewords_tfidfer.extract_keywords(text, num_keywords)

    def extract_abstract(self, text, num_sentences):
        return self.abstract_textranker.extract_abstract(text, num_sentences)
