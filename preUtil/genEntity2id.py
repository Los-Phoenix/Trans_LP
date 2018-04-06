#coding:utf-8
#这个脚本按照TransE的要求生成Entity2id
#像这样的脚本一共有5个, 生成 Relation2id
#为啥它这个跟你的好像啊

#不管,先生成再说

#在文件夹里 ../data/simplewiki/
#遍历category_inlinks, category_pages page_inlinks三个文件
#把其中的两个实体拿出来, 组成set
#先把set的大小写在头里
#再依次写set的元素,顺便编个号

categoryList = list(open("../data/simplewiki/category_inlinks.txt"))
catePageList = list(open("../data/simplewiki/category_pages.txt"))
pageList =  list(open("../data/simplewiki/page_inlinks.txt"))

cateSet = set()
pageSet = set()
for line in categoryList:
    for cate in line.split('\t'):
        cateSet.add(cate.strip())

#cate = 28078
# print(len(cateSet))


for line in catePageList:
    cate, page = line.split('\t')
    cateSet.add(cate)
    pageSet.add(page.strip())

print(len(cateSet))
print(len(pageSet))


for line in pageList:
    page1, page2 = line.split('\t')
    pageSet.add(page1.strip())
    pageSet.add(page2.strip())


print(len(cateSet))
print(len(pageSet))

uniSet = cateSet.union(pageSet)
print(len(uniSet))

print('%d%d' %(1, 1))

f_out = open("../data/simplewiki/entity2id.txt", 'w')
f_out.write("%d\n"%(len(uniSet)))

for i in range(len(uniSet)):
    f_out.write(("%s\t%d\n"%(uniSet.pop(), i)))

print(len(uniSet))