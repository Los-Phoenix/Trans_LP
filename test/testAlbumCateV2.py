# 这个测试区分类的所有子类中名字的频繁子串
#all n grams()
#ngram hit
#hit percentage

#按照HitP 从高到低，写列表 父 子数 MostHitgram HitPercentage
#需要类超过10-200个子集

from gensim.models import KeyedVectors
from test.readpage import loadAll as lop
from test.pickleModel import loadAll as lom

def ngram(strIn, num):
    #这个函数统计字符串里的所有
    rst = []
    for b in range(len(strIn) + 1):
        for e in range(b+num,len(strIn) + 1):
            rst.append(strIn[b:e])
    return rst

def ngramCount(listIn, n):
    #输入是一串字符串list
    #统计所有n元组的次数
    #返回未排序的Dict

    #先建立set
    gramSet = set()
    for i in listIn:
        # print(ngram(i))
        gramSet = gramSet.union(set(ngram(i, n)))

    # print(gramSet)
    # print("因为啥啊？输出呢")
    gramDict = dict(zip(gramSet, [-1 for i in gramSet]))
    for line in listIn:
        for sub in gramDict:
            if line.find(sub) > -1:
                gramDict[sub] += 1
    return gramDict

def maxGram(listIn, n = 1):
    subDict = ngramCount(listIn, n)
    maxSub = "Empty_Dict"
    maxCount = 0
    for sub in subDict:
        if subDict[sub] > maxCount:
            maxSub = sub
            maxCount = subDict[sub]

    return maxSub, maxCount, maxCount/len(listIn)


# model = lom()
# print("Model Loaded")
if __name__ == "__main__":
    wid_id_list = list(open('../data/wiki/entity2id.txt', 'r'))
    wid_id_dict = dict([(i.split()[0], i.split()[1].strip()) for i in wid_id_list[1:]])
    id_wid_dict = dict([(i.split()[1].strip(), i.split()[0]) for i in wid_id_list[1:]])
    print("wid_id Loaded")

    wid_cate_list = list(open('/home/losphoenix/zhwiki/output/Category.jian.txt', 'r'))
    wid_cate_dict = dict([(i.split()[0], i.split()[2].strip()) for i in wid_cate_list])
    cate_wid_dict = dict([(i.split()[2].strip(), i.split()[0]) for i in wid_cate_list])
    print("wid_cate Loaded")

    # 这个项目不需要page
    # titleList, idList, ptitle_id_dict, id_ptitle_dict = lop()
    # print("Page Loaded")
    # titleSet = set(titleList)

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

# outNoPage = open('../data/wiki/cateNoPage.txt', 'w')
# outPage = open('../data/wiki/catePage.txt', 'w')
# for cate in pDict:
#     if not wid_cate_dict[cate] in titleSet:
#         outNoPage.write(wid_cate_dict[cate] + '\n')
#     elif len(pDict[cate]) > 20 :
#         outPage.write(wid_cate_dict[cate] + '\n')
#
# outPage.close()
# outNoPage.close()

    #对于所有的category 10-200
    #生成子类的列表
    #接收返回值
    #生成列表 父 子数 MostHitgram HitPercentage
    #列表排序（sorted）
    rstList = list()
    cnt = 0
    for cate in pDict:
        sonList = [wid_cate_dict[son_wid] for son_wid in pDict[cate]]
        if len(sonList) > 200 or len(sonList) < 10:
            continue

        gStr, gHit, gHitR = maxGram(sonList, 2)
        pName = wid_cate_dict[cate]
        sNum = len(sonList)
        rstList.append([pName, str(sNum), gStr, str(gHit), str(gHitR)])
        cnt += 1
        if cnt % 100 == 0:
            print("%d cates Parsed"%(cnt))

    outList = sorted(rstList, key=lambda i:i[4])
    print("Sorted")
    outCateGram = open('../data/wiki/cateGramCount.txt', 'w')
    for i in outList:

        outCateGram.write("\t".join(i) + '\n')