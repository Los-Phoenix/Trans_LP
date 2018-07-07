#coding:utf-8

import random
from test.testAlbumCateV3 import loadAll

categoryList = list(open("/home/losphoenix/zhwiki/output/category_outlinks.txt"))
tabooSet = loadAll()

print("File read!")

wid_cate_list = list(open('/home/losphoenix/zhwiki/output/Category.jian.txt', 'r'))
wid_cate_dict = dict([(i.split()[0], i.split()[2].strip()) for i in wid_cate_list])
cate_wid_dict = dict([(i.split()[2].strip(), i.split()[0]) for i in wid_cate_list])
print("wid_cate Loaded")

outList = list()
for line in categoryList:
    cate1, cate2 = line.split('\t')
    if cate1 in tabooSet:
        print("Taboo! :", wid_cate_dict[cate1])
        continue
    outList.append([cate1, cate2.strip(), 0])

f_out = open("/home/losphoenix/zhwiki/output/train2id.txt", 'w')

random.shuffle(outList)
idx = len(outList)
cnt = 0

f_out.write("%d\n"%(idx))
ettSet = set()
for i in outList[0:idx]:
    # f_out.write(("%s\t%s\t%d\n"%(i[0], i[1], i[2])))
    ettSet.add(i[0])
    ettSet.add(i[1])
    cnt += 1

print(cnt)

f_out2 = open("/home/losphoenix/zhwiki/output/entity2id.txt", 'w')
f_out2.write("%d\n"%(len(ettSet)))

ettDict = dict(zip(list(ettSet), range(len(ettSet))))
print("Dict Got")
#print(ettDict)
for i in list(ettDict):
    f_out2.write(("%s\t%d\n"%(i, ettDict[i])))
print("Ett Written")

for i in outList[0:idx]:
    f_out.write(("%s\t%s\t%d\n"%(ettDict[i[0]], ettDict[i[1]], i[2])))
print("Train Written")