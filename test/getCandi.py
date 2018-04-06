
from test.readpage import loadAll
titleList, idList, titleDict, idDict = loadAll()

root = '../data/smk/'
c1 = root + '大学物理.seg'
c2 = root + '大学计算机基础.seg'
c3 = root + '高等数学一.seg'
c4 = root + '高等数学二.seg'

out_appen = '.candi'

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def find_candidate(titleL, word):
    #这个函数为word在titleList中返回候选，否则返回NOT_FOUND
    rst = list()
    for i in titleList:
        if i.find(word) != -1:
            rst.append(i)
    if len(rst) == 0:
        rst.append("NOT_FOUND")
    return rst

subLine = list(open(c2, 'r'))
outf = open(c2 + out_appen, 'w')
found_set = set()

for line in subLine:
    word = line.split()
    for w in word:
        if len(w) > 1 and  is_chinese(w[0]) and not w in found_set:
            found_set.add(w)
            print(w)
            candiList = find_candidate(titleList, w)
            candiString = "\t".join(candiList)
            print(candiString)
            outf.write(w + "\t" + candiString)
            outf.write("\n")

outf.flush()
outf.close()