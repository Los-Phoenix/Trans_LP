#coding:utf-8
#这个脚本按照TransE的要求生成Entity2id
#像这样的脚本一共有5个, 生成 Relation2id
#为啥它这个跟你的好像啊

#不管,先生成再说

#在文件夹里 ../data/simplewiki/
#遍历category_inlinks, category_pages page_inlinks三个文件
#每一行拿出两个实体 你固定一个类型
import random
from test.testAlbumCateV3 import loadAll
tabooSet = loadAll()

categoryList = list(open("/home/losphoenix/zhwiki/output/category_outlinks.txt"))
catePageList = list(open("/home/losphoenix/zhwiki/output/category_pages.txt"))
pageList =  list(open("/home/losphoenix/zhwiki/output/page_outlinks.txt"))

print("File read!")

wid_cate_list = list(open('/home/losphoenix/zhwiki/output/Category.jian.txt', 'r'))
wid_cate_dict = dict([(i.split()[0], i.split()[2].strip()) for i in wid_cate_list])
cate_wid_dict = dict([(i.split()[2].strip(), i.split()[0]) for i in wid_cate_list])
print("wid_cate Loaded")

outList = list()
for line in categoryList:
    cate1, cate2 = line.split('\t')
    if cate1 in tabooSet:
        print("Taboo!", wid_cate_dict[cate1])
        continue

    outList.append([cate1, cate2.strip(), 0])

#cate = 28078
print(len(categoryList))

for line in catePageList:
    cate, page = line.split('\t')
    outList.append([cate, page.strip(), 2])

print(len(catePageList))

random.shuffle(pageList)
idx = len(pageList)//10
print(idx)

for line in pageList[1:idx]:
    page1, page2 = line.split('\t')
    outList.append([page1, page2.strip(), 1])

print("PageLoaded:", idx)

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