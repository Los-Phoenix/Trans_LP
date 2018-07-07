oriVec = list(open('../data/wikiCate2/entity2vec.vec'))
print('File Read')
outF = open('../data/wikiCate2/entity2vec.vec.txt', 'w')

etts = len(oriVec)
dims = len(oriVec[0].split())
outF.write("%d %d\n"%(etts, dims))

id = 0
for i in oriVec:
    line = list([str(id)])
    line += i.split()
    # print(" ".join(line))
    outF.write(" ".join(line) + "\n")
    id += 1
    if id % 10000 == 0:
        print("Written %d Entities"%(id))