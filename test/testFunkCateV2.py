# 这个测试区分有主页面的类和没有主页面的类

from gensim.models import KeyedVectors
from test.readpage import loadAll as lop
from test.pickleModel import loadAll as lom

# model = lom()
# print("Model Loaded")

wid_id_list = list(open('../data/wiki/entity2id.txt', 'r'))
wid_id_dict = dict([(i.split()[0], i.split()[1].strip()) for i in wid_id_list[1:]])
id_wid_dict = dict([(i.split()[1].strip(), i.split()[0]) for i in wid_id_list[1:]])
print("wid_id Loaded")

wid_cate_list = list(open('/home/losphoenix/zhwiki/output/Category.jian.txt', 'r'))
wid_cate_dict = dict([(i.split()[0], i.split()[2].strip()) for i in wid_cate_list])
cate_wid_dict = dict([(i.split()[2].strip(), i.split()[0]) for i in wid_cate_list])
print("wid_cate Loaded")

titleList, idList, ptitle_id_dict, id_ptitle_dict = lop()
print("Page Loaded")
titleSet = set(titleList)

cateLink = list(open('/home/losphoenix/zhwiki/output/category_inlinks.txt', 'r'))

sonList = list(set([i.split()[0] for i in cateLink]))
sonDict = dict(zip(sonList, [[] for i in sonList]))

for i in cateLink:
    i0, i1 = i.split()
    sonDict[i0].append(i1.strip())

cateOut = list(open('/home/losphoenix/zhwiki/output/category_outlinks.txt', 'r'))
pList = list(set([i.split()[0] for i in cateOut]))
pDict = dict(zip(pList, [[] for i in pList]))

for i in cateOut:
    i0, i1 = i.split()
    pDict[i0].append(i1.strip())

print('inLink Read!!')

outNoPage = open('../data/wiki/cateNoPage.txt', 'w')
outPage = open('../data/wiki/catePage.txt', 'w')
for cate in pDict:
    if not wid_cate_dict[cate] in titleSet:
        outNoPage.write(wid_cate_dict[cate] + '\n')
    elif len(pDict[cate]) > 20 :
        outPage.write(wid_cate_dict[cate] + '\n')

outPage.close()
outNoPage.close()