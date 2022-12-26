import pandas as pd
import numpy as np
import jieba
import sys
import jieba.analyse
import  xlwt
import codecs
import os
from string import punctuation

dir_path = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(r'C:\Users\28277\Desktop\开源软件基础\MailListTitle.csv')

with open('Mailing list topic.txt',mode='a',encoding='utf-8') as file:
            for line in df.values:
                file.write(str(line))

print('write finished')

#创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

#对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stop_word.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

inputs = open('Mailing list topic.txt','r',encoding='utf-8')
outputs = open('sentence_seged Mailing list topic.txt','w',encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)
    outputs.write(line_seg+'\n')
outputs.close()
inputs.close()

#统计词频
def count():
    file=open("sentence_seged Mailing list topic.txt",'r')
    wordCounts={}    #先建立一个空的字典，用来存储单词 和相应出现的频次
    count=10         #显示前多少条（按照单词出现频次从高到低）
    for line in file:
        lineprocess(line.lower(),wordCounts)  #对于每一行都进行处理，调用lineprocess()函数，参数就是从file文件读取的一行
        items0=list(wordCounts.items())       #把字典中的键值对存成列表，形如：["word":"data"]
        items=[[x,y] for (y,x) in items0]     #将列表中的键值对换一下顺序，方便进行单词频次的排序 就变成了["data":"word"]
        items.sort()            #sort()函数对每个单词出现的频次按从小到大进行排序

    for i in range(len(items)-1,len(items)-count-1,-1):   #上一步进行排序之后 对items中的元素从后面开始遍历 也就是先访问频次多的单词
            print(items[i][1]+"\t"+str(items[i][0]))




def lineprocess(line,wordCounts):
    for ch in line:   #对于每一行中的每一个字符 对于其中的特殊字符需要进行替换操作
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line=line.replace(ch,"")
    words=line.split()  #替换掉特殊字符以后 对每一行去掉空行操作,也就是每一行实际的单词数量
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1

    #这个函数执行完成之后整篇文章里每个单词出现的频次都已经统计好了

count()
