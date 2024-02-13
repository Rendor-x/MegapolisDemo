def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f=open(namefile,'r',encoding='utf-8')
    students=[]
    for i in range(501):
        students.append(f.readline().strip().split(','))
        if students[i][4]=='None':
            students[i][4]='0'
    return students


def new_marks(ls):
    list_of_classes = []
    for i in range(1, 501):
        if ls[i][4] == '0':
            list_of_classes.append(ls[i][3])
    dc = {i: [] for i in list_of_classes}
    for i in list_of_classes:
        for j in range(1, 501):
            if ls[j][3] == i and ls[j][4] != '0':
                dc[i].append(int(ls[j][4]))
    for i in dc:
        dc[i] = format(sum(dc[i]) / len(dc[i]), '.3f')
    for i in range(1, 501):
        if ls[i][4] == '0':
            ls[i][4] = dc[ls[i][3]]


def writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0])+'\n')
    for i in range(500):
        f.write(','.join(students[i]) + '\n')
    f.close()


students = readfile('/home/teacher/Загрузки/students.csv')
new_marks(students)
writefile('student_new_1.csv')
