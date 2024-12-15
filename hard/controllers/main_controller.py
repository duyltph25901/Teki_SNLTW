from controllers.feature_controller import saveInformationRecord, fetchAllStudents, updateStudentById, deleteStudentById, sortAvgDesc, sortAvgAsc, searchStudentByName

featureAddStudent = 1
featureShowAll = 2
featureUpdate = 3
featureDelete = 4
featureSortAvgDesc = 5
featureSortAvgAsc = 6
featureFilterAgeDesc = 7
featureFilterAgeAsc = 8
featureSearchByName = 9
featureExit = 0

def validateFeatureInput(featureIndex):
    check = True
    featureIndexNumber = 0

    try:
        featureIndexNumber = int(featureIndex)

        if (featureIndexNumber < 0) or (featureIndexNumber > 9): check = False
    except ValueError as e:
        check = False

    return check

def switchCase(index):
    if (index == featureAddStudent): saveInformationRecord()
    elif (index == featureShowAll): fetchAllStudents()
    elif (index == featureUpdate): updateStudentById()
    elif (index == featureDelete): deleteStudentById()
    elif (index == featureSortAvgDesc): sortAvgDesc()
    elif (index == featureSortAvgAsc): sortAvgAsc()
    elif (index == featureSearchByName): searchStudentByName()