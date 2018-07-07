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
from test.testAlbumCateV3 import loadAll as lot

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
# root = "电脑"
# outF = open("noLoopV3.log", 'w')
root = "数学"
outF = open("noLoopV3math.log", 'w')
wid_root = cate_wid_dict[root]
# print(wid)
# pl = pDict[wid]
# print(pl)
# for p in pl:
#     print(wid_cate_dict[p])

#不加禁止表的宽搜
#使用list 和headptr
# 增加"已完全扩展"
# 增加“route”
c_wid_list = list(wid_cate_dict.keys())
c2Dict = dict(zip(c_wid_list, [[] for i in c_wid_list]))
c2Dict[wid_root].append(['r'])# 这是一个字符串的二维list

q = [wid_root]
e_set= set()
start_ptr = 0
taboo_set = lot()


while start_ptr < len(q):
    q_n = q[start_ptr]
    start_ptr += 1
    if q_n in e_set:
        print('YOU again?')
        continue
    if q_n in pDict.keys():
        s_q_n = pDict[q_n]
    else:
        continue

    for s in s_q_n:
        outF.write("==={} {} ===\n".format(s, wid_cate_dict[s]))
        if s in taboo_set:
            print("禁断：")
            print(s, wid_cate_dict[s])
            outF.write("==={} {} ===\n".format(s, wid_cate_dict[s]))
            outF.write("\t禁止的\n")
            continue
        if q_n == s:
            print("WOW, HJJ!")
            print(s, wid_cate_dict[s])
            outF.write("==={} {} ===\n".format(s, wid_cate_dict[s]))
            outF.write("\t自引用的\n")
            continue
        for r in c2Dict[q_n]:
            r_new = list([wid_cate_dict[s]])
            r_new.extend(r)
            c2Dict[s].append(r_new)
        print("\t", s, wid_cate_dict[s])
        # outF.write("==={} {} ===\n".format(s, wid_cate_dict[s]))
        for r in c2Dict[s]:
            outF.write("\t{}\n".format("<-".join(r)))
        q.append(s)
    e_set.add(q_n)