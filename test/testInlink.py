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

model = lom()
print("Model Loaded")

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

qlist = [
    "C语言",
    "娱乐",
    "大学",
    "人工智能",
    "语文考试",
    "量子力学",
    "相对论",
    "生物系统",
    "系统生物学",
    "物理学家"
]

for qq in qlist:
    print("=====%s====="%(qq))
    if qq in cate_wid_dict:
        inList = sonDict[cate_wid_dict[qq]]
        for i in inList:
            wid = i
            if wid in wid_cate_dict:
                name = "Cate: " + wid_cate_dict[wid]
            else:
                name = "Page: " + id_ptitle_dict[wid]
            print(name, model.similarity(wid_id_dict[cate_wid_dict[qq]], wid_id_dict[wid]))
