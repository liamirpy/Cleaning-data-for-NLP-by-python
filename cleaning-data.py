###AMIR MOSAVI///LIAMIRPY 
import pandas as pd
import numpy as np
import csv

df=pd.read_excel(r'digi.xlsx')
df.dropna(inplace=True)
##############STOP WORDS
stop_word_csv = pd.read_csv('persian_stopwords.csv')
stop_word_csv1 = stop_word_csv.values.tolist()
stop_words_list1 = []
for i in range(len(stop_word_csv1)):
    stop_words_list1.append(stop_word_csv1[i][0])
s = open('stopwords.txt', 'r')
stop = s.read().lower()
s.close()
line = stop.replace('\n', ' ')
lines = line.replace('.', ' ')
stop_words_list2 = lines.split(' ')
stop_words= stop_words_list2 + stop_words_list1

def delet_stop_words(text):
    text_without_stopwords=[]
    for j in range(len(text)):
        if not text[j] in stop_words:
            text_without_stopwords.append(text[j])
    return text_without_stopwords

list_title=list(df['title_en'])
unique=[]
for i in list_title:
    if i not in unique:
        unique.append(i)
    else:
        continue

unique_dictionary={}
for title in unique:
    ind=[]
    for i,j in enumerate(list_title):
        if j==title:
           ind.append(i)

    com=[]
    for i in ind:
        com.append(df.values[i][1])
    for u in range(len(com)):
        com[u] = com[u].replace('._x000D_', ' ')
        com[u] = com[u].replace('_x000D_', ' ')
        com[u] = com[u].replace('😊', ' ')
        com[u] = com[u].replace('😉', ' ')
        com[u] = com[u].replace('😐', ' ')
        com[u] = com[u].replace('😐', ' ')
        com[u] = com[u].replace('😍', ' ')
        com[u] = com[u].replace('😎', ' ')
        com[u] = com[u].replace('😋', ' ')
        com[u] = com[u].replace('😇', ' ')
        com[u] = com[u].replace('❤', ' ')
        com[u] = com[u].replace('😂', ' ')
        com[u] = com[u].replace('2.0', ' ')
        com[u] = com[u].replace('3.5', ' ')
        com[u] = com[u].replace(')', ' ')
        com[u] = com[u].replace('\n', ' ')
        com[u] = com[u].replace('❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤😍😍😍😍😍😍😍😍', ' ')
    unique_dictionary[title]=delet_stop_words(com)
    unique_dictionary[title]=' '.join(unique_dictionary[title])


with open('title.csv','w') as f:
    w = csv.writer(f)
    row = ['title_en', 'comment']
    w.writerow(row)
    w.writerows(unique_dictionary.items())
f.close()
