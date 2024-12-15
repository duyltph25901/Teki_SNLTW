from controllers.utils_controller import generateId
from models.entity.student_entity import Student
from prettytable import PrettyTable

students = []

def saveInformationRecord():
    idLen = 12
    id = generateId(idLen)
    studentName = ""
    ageTypeStr = ""
    address = ""
    avgPointTypeStr = ""

    ageTypeNumber = 0
    avgPointTypeNumber = 0.0

    # Validate student name and set value to student name
    while True:
        studentName = input("\tTên học sinh: ")
        isStudentNameOke = validateStudentName(studentName)
        if isStudentNameOke: break
        else: print("\t>>>>> Tên không hợp lệ, vui lòng nhập lại! <<<<<")

    # Validate student age and set value to student age
    while True:
        ageTypeStr = input("\tSố tuổi học sinh: ")
        isStudentAgeOke = validateStudentAge(ageTypeStr)
        if isStudentAgeOke: 
            ageTypeNumber = int(ageTypeStr)
            break
        else: print("\t>>>>> Tuổi học sinh không hợp lệ, vui lòng nhập lại! <<<<<")

    # Validate student address and set value to student address
    while True:
        address = input("\tĐịa chỉ cư chú: ")
        isAddressOke = validateAddress(address)
        if (isAddressOke): break
        else: print("\t>>>>> Địa chỉ không hợp lệ, vui lòng nhập lại! <<<<<")
    
    # Validate student avg point and set value to student avg point
    while True:
        avgPointTypeStr = input("\tĐiểm trung bình: ")
        isAvgPointOke = validateAvgPoint(avgPointTypeStr)
        if isAvgPointOke: 
            avgPointTypeNumber = float(avgPointTypeStr)
            break
        else: print("\t>>>>> Điểm trung bình không hợp lệ, vui lòng nhập lại! <<<<<")

    student = Student(
        id = id,
        studentName = studentName,
        age = ageTypeNumber,
        address = address,
        avgPoint = avgPointTypeNumber
    )
    students.append(student)
    print(f"\n\t-> Thông tin đã lưu:\n\t\tId: {id}\n\t\tName: {studentName}\n\t\tAge: {ageTypeNumber}\n\t\tAddress: {address}\n\t\tAvg Point: {avgPointTypeNumber}")

def validateStudentName(name):
    if (len(name) == 0): return False
    else:
        return len(name) >= 2

def validateStudentAge(age):
    try: 
        ageNumber = int(age)

        return ageNumber >= 6 and ageNumber <= 18
    except ValueError as e:
        return False
    
def validateAddress(address):
    return len(address) >= 2

def validateAvgPoint(point):
    try:
        pointTypeNumber = float(point)

        return pointTypeNumber >= 0.0 and pointTypeNumber <= 10.0
    except ValueError as e:
        return False

def fetchAllStudents():
    table = PrettyTable()
    table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
    for student in students:
        table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

    print("\tDanh sách học sinh:")
    print(table)

def updateStudentById():
    idStudent = ""
    while (True):
        idStudent = input('\tNhập mã học sinh cần thay đổi (Nhập "HUY" để quay lại chức năng khác): ')
        if (str("HUY").lower() == str(idStudent).strip().lower()):
            print("\t\t---> Đã dừng chức năng cập nhật học sinh theo Id!")
            return
        else: 
            validateId = validateIdStudentIdNumber(idStudent)
            if (validateId): break
            else: print("\t>>>>> Mã học sinh không hợp lệ, vui lòng nhập lại! <<<<<")

    # Validate student name and set value to student name
    while True:
        studentName = input("\tTên học sinh: ")
        isStudentNameOke = validateStudentName(studentName)
        if isStudentNameOke: break
        else: print("\t>>>>> Tên không hợp lệ, vui lòng nhập lại! <<<<<")

    # Validate student age and set value to student age
    while True:
        ageTypeStr = input("\tSố tuổi học sinh: ")
        isStudentAgeOke = validateStudentAge(ageTypeStr)
        if isStudentAgeOke: 
            ageTypeNumber = int(ageTypeStr)
            break
        else: print("\t>>>>> Tuổi học sinh không hợp lệ, vui lòng nhập lại! <<<<<")

    # Validate student address and set value to student address
    while True:
        address = input("\tĐịa chỉ cư chú: ")
        isAddressOke = validateAddress(address)
        if (isAddressOke): break
        else: print("\t>>>>> Địa chỉ không hợp lệ, vui lòng nhập lại! <<<<<")
    
    # Validate student avg point and set value to student avg point
    while True:
        avgPointTypeStr = input("\tĐiểm trung bình: ")
        isAvgPointOke = validateAvgPoint(avgPointTypeStr)
        if isAvgPointOke: 
            avgPointTypeNumber = float(avgPointTypeStr)
            break
        else: print("\t>>>>> Điểm trung bình không hợp lệ, vui lòng nhập lại! <<<<<")

    student = Student(
        id = idStudent,
        studentName = studentName,
        age = ageTypeNumber,
        address = address,
        avgPoint = avgPointTypeNumber
    )
    indexStudentUpdate = searchIndexStudentById(idStudent)
    students[indexStudentUpdate] = student
    print(f"\tThông tin của học sinh có Id là {student.id} đã được thay đổi!")
    
def validateIdStudentIdNumber(id):
    if (len(str(id)) == 0):
        return False
    else:
        try: 
            idNumber = int(id)
            searchResult = False

            for student in students:
                if (student.id == idNumber): 
                    searchResult = True
                    break

            return searchResult
        except ValueError as valueError:
            return False
        
def searchIndexStudentById(id):
    for i in range(len(students)):
        if (str(students[i].id) == str(id)):
            return i
        
    return 0

def deleteStudentById():
    idStudent = ""
    while (True):
        idStudent = input('\tNhập mã học sinh cần xóa (Nhập "HUY" để quay lại chức năng khác): ')
        if (str("HUY").lower() == str(idStudent).strip().lower()):
            print("\t\t---> Đã dừng chức năng xóa học sinh theo Id!")
            return
        else: 
            validateId = validateIdStudentIdNumber(idStudent)
            if (validateId): break
            else: print("\t>>>>> Mã học sinh không hợp lệ, vui lòng nhập lại! <<<<<")

    indexStudent = searchIndexStudentById(int(idStudent))
    students.pop(indexStudent)
    print(f"\tThông tin của học sinh có Id là {idStudent} đã được xóa!")

def sortAvgDesc(): 
    sortedStudents = sorted(students, key=lambda student: student.avgPoint, reverse=True)
    table = PrettyTable()
    table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
    for student in sortedStudents:
        table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

    print("\tDanh sách học sinh sắp xếp theo điểm giảm dần:")
    print(table)

def sortAvgAsc(): 
    sortedStudents = sorted(students, key=lambda student: student.avgPoint, reverse=False)
    table = PrettyTable()
    table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
    for student in sortedStudents:
        table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

    print("\tDanh sách học sinh sắp xếp theo điểm tăng dần:")
    print(table)

def sortAgeDesc():
    sortedStudents = sorted(students, key=lambda student: student.age, reverse=True)
    table = PrettyTable()
    table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
    for student in sortedStudents:
        table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

    print("\tDanh sách học sinh sắp xếp theo tuổi giảm dần:")
    print(table)

def sortAgeAsc():
    sortedStudents = sorted(students, key=lambda student: student.age, reverse=False)
    table = PrettyTable()
    table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
    for student in sortedStudents:
        table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

    print("\tDanh sách học sinh sắp xếp theo tuổi giảm dần:")
    print(table)

def searchStudentByName():
    studentName = ""
    # Validate student name and set value to student name
    while True:
        studentName = input("\tTên học sinh: ")
        isStudentNameOke = validateStudentName(studentName)
        if isStudentNameOke: break
        else: print("\t>>>>> Tên không hợp lệ, vui lòng nhập lại! <<<<<")

    arrResult = handleSearchStudentByName(studentName)
    isResultNull = len(arrResult) == 0

    if (isResultNull):
        print("\t\t---> Không tìm thấy học sinh trong danh sách!")
    else: 
        table = PrettyTable()
        table.field_names = ["Id", "Student Name", "Age", "Address", "Avg Point"]
        for student in arrResult:
            table.add_row([student.id, student.studentName, student.age, student.address, student.avgPoint])

        print("\tDanh sách học sinh đã tìm kiếm:")
        print(table)


def handleSearchStudentByName(name):
    arrResult = []
    for student in students:
        if (str(name).lower() in str(student.studentName).lower()):
            arrResult.append(student)

    return arrResult