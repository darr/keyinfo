#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : sentence_similarity.py
# Create date : 2019-08-05 16:13
# Modified date : 2019-08-05 16:44
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

import gensim
import numpy as np

class SimilarityCompute:
    def __init__(self):
        self.embedding_file = 'data/token_vector.bin'
        self.model = gensim.models.KeyedVectors.load_word2vec_format(self.embedding_file, binary=False)

    def get_wordvector(self, word):
        try:
            return self.model[word]
        except:
            return np.zeros(200)

    def similarity_cosine(self, word_list1,word_list2):
        simalrity = 0
        vector1 = np.zeros(200)
        for word in word_list1:
            vector1 += self.get_wordvector(word)

        vector1 = vector1/len(word_list1)
        vector2 = np.zeros(200)

        for word in word_list2:
            vector2 += self.get_wordvector(word)

        vector2 = vector2/len(word_list2)
        cos1 = np.sum(vector1*vector2)
        cos21 = np.sqrt(sum(vector1**2))
        cos22 = np.sqrt(sum(vector2**2))
        similarity = cos1/float(cos21*cos22)
        return similarity
