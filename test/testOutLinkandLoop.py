#这个文件可以看“计算机”类相似的实体都是什么
#需要page_wid, cate_wid
#wid_id
#id_wid
#wid_page
#wid_cate
#把i处理一下输出

from gensim.models import KeyedVectors
from test.readpage import loadAll as lop
from test.pickleModel import loadAll as lom

# model = lom()
# print("Model Loaded")

wid_id_list = list(open('../data/wikiCate2/entity2id.txt', 'r'))
wid_id_dict = dict([(i.split()[0], i.split()[1].strip()) for i in wid_id_list[1:]])
id_wid_dict = dict([(i.split()[1].strip(), i.split()[0]) for i in wid_id_list[1:]])
print("wid_id Loaded")

wid_cate_list = list(open('/home/losphoenix/zhwiki/output/Category.jian.txt', 'r'))
wid_cate_dict = dict([(i.split()[0], i.split()[2].strip()) for i in wid_cate_list])
cate_wid_dict = dict([(i.split()[2].strip(), i.split()[0]) for i in wid_cate_list])
print("wid_cate Loaded")

titleList, idList, ptitle_id_dict, id_ptitle_dict = lop()
print("Page Loaded")

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


print(len(wid_cate_dict.keys()))
print(len(pDict.keys()))
#在category_outlinks上遍历，打印结果
#如果发现了圈，打印圈
#如果发现可疑的扩展，打印扩展
root = "电脑"

wid_root = cate_wid_dict[root]
# print(wid)
# pl = pDict[wid]
# print(pl)
# for p in pl:
#     print(wid_cate_dict[p])

#不加禁止表的宽搜
#使用list 和headptr
#那么开始吧

q = [wid_root]
start_ptr = 0
while start_ptr < len(q):
    q_n = q[start_ptr]
    if q_n in pDict.keys():
        s_q_n = pDict[q_n]
    for s in s_q_n:
        print(s, wid_cate_dict[s])
        q.append(s)
    start_ptr += 1
# 毫无终止的无限循环