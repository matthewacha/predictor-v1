import operator
import random
import gensamples
import math

"""collect all data and separate into test and training data
trainData: is the datawhose parameters are used to determine k nearest neighbours
testData: is the data we feed in to the algorith so it can predict based on its parameters"""

data=gensamples.genCreatures(6000)

def prepData(data,factor,testData=[],trainData=[]):
	all_data=data
	for x in range(len(all_data)):
		if len(testData) <= len(all_data)*factor:
			selected=random.choice(all_data)
			if selected in testData:
				trainData.append(selected)
			else:
				testData.append(selected)
		else:
			selected=all_data[x]
			if selected not in trainData:
				trainData.append(selected)
	
#find euclidean distance of testinstance to all points in test sample

def euclidist(case1,case2,length_of_data):
	distances=[pow((case1[x]-case2[x]),2) for x in range(1,length_of_data)]
	return math.sqrt(sum(distances))

#find k nearest neighbor

def nearest_neighbors(testInstance,trainData, k):
	length_of_data=len(testInstance)
	distance=[(trainData[x][0],euclidist(testInstance,trainData[x],length_of_data)) for x in range(len(trainData)) ]
	distance.sort(key=operator.itemgetter(1), reverse=False)
	neighbours=[distance[i] for i in range(k)]
	return neighbours
	
#use k nearest neigbors to select neighborhood/class

def selectClass(neighbours):
	selectedClass={}
	for x in range(len(neighbours)):
		result=neighbours[x][0]
		if result in selectedClass:
			selectedClass[result] +=1
		else:
			selectedClass[result]=1
	return sorted(selectedClass.items(),key=operator.itemgetter(1), reverse=True)[0][0]
	
#determine accuracy
def accuracy(predictions,testCase):
	result=[x for x in range(len(testCase)) if predictions[x]==testCase[x][0]]
	return (len(result)/float(len(testCase)))*100.0

#prediction method
def predictor():
	testData=[]
	trainData=[]
	factor=0.75
	k=5
	predictions=[]
	prepData(data,factor,testData,trainData)
	for x in range(len(testData)):
		neighbours=nearest_neighbors(testData[x],trainData, k)
		result=selectClass(neighbours)
		prediction=result
		predictions.append(prediction)
		print ' {}: predicted: {}, Actual: {}'.format(x,result,testData[x][0])
	prediction_accuracy=accuracy(predictions,testData)
	print '\n All Data: {} \n testData: {} \n trainigData: {} \n Prediction Accuracy: {}% \n '.format(len(data),len(testData), len(trainData), prediction_accuracy)
	
	
predictor()
