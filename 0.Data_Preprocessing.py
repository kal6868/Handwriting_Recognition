################################### Text Recognition Data Generator 사용 ##############################################
#pip install trdg
#pip install -r C:/Users/Anony/Downloads/TextRecognitionDataGenerator-master/requirements.txt

import os
import pandas as pd
from trdg.generators import (GeneratorFromDict, GeneratorFromRandom, GeneratorFromStrings, GeneratorFromWikipedia)
file = 'C:/Users/Anony/Downloads/TextRecognitionDataGenerator-master/trdg/dicts/ko.txt' #완성형 한글 2350자
with open(file, 'r', encoding='utf-8') as wordtxt:
    a = wordtxt.readlines()

word = []
for i in range(0,len(a)):
    word.append(a[i].split()[0])
len(word)

gw = os.getcwd()
base = os.path.join(os.getcwd(), 'workspace2')
Gen_Data = os.path.join(os.getcwd(), 'workspace2/Data/Gen_Data')

try:
    if not os.path.exists(Gen_Data):
        os.makedirs(Gen_Data)

except OSError:
    pass

generator_train = GeneratorFromStrings(word, count = 100000, language='ko')
i = 1
for img, lbl in generator_train:
    img.save(Gen_Data + '/' + lbl + '_' + str(i).zfill(6)  + '.jpg')
    i += 1
################################# CSV 파일 만들기 ############################
# 1. TRGD_DATA
from tqdm import tqdm
import os
gd = os.path.join(os.getcwd(), 'workspace2\\Data\\Gen_Data')
hw1s = os.path.join(os.getcwd(), 'workspace2\\Data\\hw_1_syllable')
hw2s = os.path.join(os.getcwd(), 'workspace2\\Data\\hw_2_syllable')
pws = os.path.join(os.getcwd(), 'workspace2\\Data\\pw_syllable')

list = os.listdir(gd)
gd_file = []
for i in tqdm(range(0, len(os.listdir(gd)))):
    path = gd + '\\' + list[i]
    syllable = list[i][0]
    comb = [path, syllable]
    gd_file.append(comb)

# 2. AI_Hub Data
##AI HUB MetaData
import json
with open('./workspace2/Data/handwriting_data_info1.json', 'r', encoding='utf-8') as hw:
    hwd = json.load(hw)

# handwriting_data
hw_anoo = hwd['annotations']
wd_list_hw = []
num_list = []
word_list = []
for i in range(0,len(hw_anoo)):
    if hw_anoo[i]['attributes']['type'] == '글자(음절)':
        wd_list_hw.append(hw_anoo[i])
        num_list.append(hw_anoo[i]['id'])
        word_list.append(hw_anoo[i]['text'])
    else:
        continue

# 1_syllable 폴더 내 파일 읽어오기
hw1s_file = []
list = os.listdir(hw1s)
for i in tqdm(range(0,len(os.listdir(hw1s)))):
    if list[i] in list:
        path = hw1s + '\\' + list[i]
        number = num_list.index(list[i][:-4])
        text = word_list[number]
        hw1s_file.append([path, text])

# 2_syllable 폴더 내 파일 읽어오기
hw2s_file = []
list = os.listdir(hw2s)
for i in tqdm(range(0,len(os.listdir(hw2s)))):
    if list[i] in list:
        path = hw2s + '\\' + list[i]
        number = num_list.index(list[i][:-4])
        text = word_list[number]
        hw1s_file.append([path, text])

# printed_data
with open('./workspace2/Data/printed_data_info.json', 'r', encoding='utf-8') as pw:
    pwd = json.load(pw)
pw_anoo = pwd['annotations']
pw_list_pw = []
num_list = []
word_list = []
for i in range(0,len(pw_anoo)):
    if pw_anoo[i]['attributes']['type'] == '글자(음절)':
        pw_list_pw.append(hw_anoo[i])
        num_list.append(pw_anoo[i]['id'])
        word_list.append(pw_anoo[i]['text'])
    else:
        continue

# syllable 폴더 내 파일 읽어오기
list = os.listdir(pws)
pw_file = []
for i in tqdm(range(0,len(os.listdir(pws)))):
    if list[i] in list:
        path = pws + '\\' + list[i]
        number = num_list.index(list[i][:-4])
        text = word_list[number]
        pw_file.append([path, text])

final_list = gd_file + hw1s_file + hw2s_file + pw_file

# 데이터 프레임으로 합치기
import pandas as pd
iden = []
for i in range(0, len(final_list)):
    iden.append(i)
df_iden = pd.DataFrame(iden, columns=[''])
df_final_list = pd.DataFrame(final_list, columns=['ids', 'labels'])
df_complete = pd.concat([df_iden, df_final_list], axis = 1)


makecsv = df_complete.copy()
makecsv.to_csv('train_data.csv', sep = ',', encoding = 'utf-8-sig', index=False)
makecsv.to_csv('train_data_backup.csv', sep = ',', encoding = 'utf-8-sig', index=False)

# 2350자만 고르기
import pandas as pd
from tqdm import tqdm
train_data = pd.read_csv('train_data.csv')

train_data_2350 = []
for i in tqdm(range(0, len(train_data))):
    if train_data['labels'][i] in word:
        train_data_2350.append((list(train_data.iloc[i])))
    else:
        continue

df_train_data_2350 = pd.DataFrame(train_data_2350, columns=['', 'ids', 'labels'])
df_train_data_2350.to_csv('train_data_2350.csv', sep = ',', encoding = 'utf-8-sig', index=False)