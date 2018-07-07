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

qlist = [
    "C语言",
    "娱乐",
    "大学",
    "计算机科学",
    "软件",
    "量子力学",
    "相对论",
    "电脑",
    "使用Catnav的页面",
    "物理学家"
]

for qq in qlist:
    print("=====%s====="%(qq))
    if not qq in cate_wid_dict:
        print("Tabooed!")
        continue
    if not cate_wid_dict[qq] in wid_id_dict:
        print("What?")
        continue
    if wid_id_dict[cate_wid_dict[qq]] in model:
        q = model.most_similar(wid_id_dict[cate_wid_dict[qq]], topn = 20)
        # q = model.most_similar(wid_id_dict[ptitle_id_dict[qq]], topn = 200)
        for e in q:
            wid = id_wid_dict[e[0]]
            if wid in wid_cate_dict:
                name = "Cate: " + wid_cate_dict[wid]
            else:
                name = "Page: " + id_ptitle_dict[wid]
            print(name, e[1])
    else:
        print("not in model?")
    print("==========\n")
