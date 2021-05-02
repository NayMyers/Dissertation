#Used to find X most likely predictions from a prediction array created by keras
#CNN model
def topClasses(self, predictionArray, xClasses=3):
    predictDict = {} #key = original array position & therefore class number
                     #value = prediction likelehood
    topClasses = []#values to return from the function
    #we zip the array into a dictionary to keep track of the values original position
    #as this correlates to the predicted class.
    for idx, prediction in enumerate(predictionArray):
        predictDict[idx] = predictionArray
    #we sort the dictionary in ascending order by value.
    #then we take the first X entries of the sorted dictionary.
    #and take the virst value i.e. class-number from the entries, as each entry
    #is a tuple, key,value pair.
    for entries in list(sorted(predictDict.items(),
    key=operator.itemgetter(1),
    reverse=True))[0:xClasses]:
        topClasses.append(entries[0])
    return topClasses
