import pickle as pickle
from gensim.models import KeyedVectors

if __name__ == '__main__':
    model = KeyedVectors.load_word2vec_format('../data/wikiCate2/entity2vec.vec.txt', binary=False)
    print("Model Loaded")

    print('Dump Start')
    f1 = open('../data/modelC2.pkl', 'wb')
    pickle.dump(model, f1, True)
    f1.close()
    print('Dump Done')

def loadAll():
    #returns vocab, embd, y, x, x_other
    print("load Model start")
    f = open('../data/modelC2.pkl', 'rb')
    model = pickle.load(f)
    f.close()
    print("load Model done!")
    return model