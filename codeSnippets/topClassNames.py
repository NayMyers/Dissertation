#given an array of class values. Get the corresponding class name from keras
#model.info JSON file.
def determineClassNames(self, classArray):
    classNames = [] #
    for classNum in classArray:
        classNum = int(classNum)
        for key, value in self.cropClasses.items():
            if classNum == value:
                classNames.append(key)

    if len(classNames) < len(classArray):
        return "one or more invalid class numbers"
    else:
        return classNames
