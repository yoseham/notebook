import numpy as np
import operator

def createDataset():
    features = np.random.randint(0,10,(4,2))
    labels = ['A','A','B','B']
    return features,labels

def classify0(inx,dataset,labels,k):
    datasetSize = dataset.shape[0]
    diffMat = np.tile(inx,(datasetSize,1))-dataset
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]