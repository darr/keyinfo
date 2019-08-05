#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-05 16:19
# Modified date : 2019-08-05 16:40
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from keyinfo import KeyInfoExtract

def run():
    nlp = KeyInfoExtract()

    text = '''
    凤凰网房产快讯8月5日，地产股难掩“跌跌不休”之势。截至15点，佳兆业美好、中国奥园、花样年控股、世茂房地产、新城控股发展、弘阳地产等10余家房企股价跌幅超5%，此外，万科、美地置业、保利地产、远洋集团、金科股份等龙头房企股价也有不同程度的下跌。
    继7月30日中共中央政治局召开会议，不将房地产作为短期刺激经济的手段，地产股自此成为重灾区。受外部市场影响，地产股亦是“雪上加霜”，此外，市场环境严苛之下，凤凰网房产了解到，亦有龙头房企内部发文称原则上暂停拿地，促销售，抓回款。
    '''
    print(text)

    keywords_textrank = nlp.extract_keywords_textrank(text, 10)
    keywords_tfidf = nlp.extract_keywords_tfidf(text, 10)
    abstract_textrank = nlp.extract_abstract(text, 3)

    print("tfidf keywords:")
    print(keywords_tfidf)
    print("textrand keywords:")
    print(keywords_textrank)
    print("abstract textrank:")
    print(abstract_textrank)

run()
