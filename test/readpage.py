import pickle as pickle




if __name__ == '__main__':
    wikipage = open('/home/losphoenix/zhwiki/output/Page.jian.txt', 'r')
    pagelist = list(wikipage)
    titleList = list()
    idList = list()
    for i in pagelist:
        _, id, title, text = i.split('\t')[:4]
        titleList.append(title)
        idList.append(id)

    titleDict = dict(zip(titleList, idList))
    idDict = dict(zip(idList, titleList))

    print('Dump Start')
    f1 = open('../data/pageDict.pkl', 'wb')
    pickle.dump(titleList, f1, True)
    pickle.dump(idList, f1, True)
    pickle.dump(titleDict, f1, True)
    pickle.dump(idDict, f1, True)
    f1.close()
    print('Dump Done')

def loadAll():
    #returns vocab, embd, y, x, x_other
    print("load pageDict start")
    f = open('../data/pageDict.pkl', 'rb')
    titleList = pickle.load(f)
    idList = pickle.load(f)
    titleDict = pickle.load(f)
    idDict = pickle.load(f)
    f.close()
    print("load pageDict done!")
    return titleList, idList, titleDict, idDict