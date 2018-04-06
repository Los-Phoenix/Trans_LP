import pickle as pickle

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
#
# for k in pDict.keys():
#     print(k, pDict[k])

