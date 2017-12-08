class Coursework2:

    def setLike(self):
        print("Exercise 1 - Containment relations of lists")
        print("1.1 Set-like containment\n")

        A = []
        B = []

        # User input to define number of elements in list and what those elements are
        listLength = int(input("Enter number of elements in list A: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        listLength = int(input("Enter number of elements in list B: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            B.append(addElement)
            listLength -= 1

        # Testing if elements in list B appear in A, in any order
        if set(B) < set(A):
            print("\nYes")
            print("List is a set-like containment\n")
        else:
            print("\nNo")
            print("List is not a set-like containment\n")

    def sequenceLike(self):
        print("-----------------")
        print("1.2 Sequence-like containment\n")

        A = []
        B = []

        listLength = int(input("Enter number of elements in list A: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        listLength = int(input("Enter number of elements in list B: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            B.append(addElement)
            listLength -= 1


        x, y = 0, 0
        while x < len(A) and y < len(B):
            # Testing if the corresponding indexes of elements within list A and B are the same
            if A[x] == B[y]:
                y += 1
            x += 1

        if y == len(B):
            print("\nYes")
            print("List is a sequence-like containment\n")
        else:
            print("\nNo")
            print("List is not a sequence-like containment\n")

    def consecutiveSequence(self):
        print("-----------------")
        print("1.3 Consecutive sequence-like containment \n")

        A = []
        B = []

        listLength = int(input("Enter number of elements in list A: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        listLength = int(input("Enter number of elements in list B: "))
        while listLength > 0:
            addElement = str(input("Enter element %d: " % (listLength)))
            B.append(addElement)
            listLength -= 1

        # Testing if all elements in list B are within list A within the range of the length of list B
        if any(B[:] == A[x:x + len(B)] for x in range(len(A) - 1)):
            print("\nYes")
            print("List is a consecutive sequence-like containment\n")
        else:
            print("\nNo")
            print("List is not a consecutive sequence-like containment\n")

    def composingReports(self):
        print("Exercise 2 - Composing module and student reports\n")
        
        # defining the variables to be placed inside the functions
        print("Original Table including negative entries:\n")
        table = [[5, -2, 3, 8],
                [5, 5, -6, 33],
                [7, 8, 9, 5, 9, 11]]
        
        # Printing out list of lists in tabular format 
        for x in range(len(table)):
            print(str(table[x::3]).replace('[', '').replace(']', ''))

        """Iterating over table list of lists and changing values less than 0
        to 0, in order to preserve equal length in column and row, and also to
        ignore negative entries"""
        
        # Seperate functions which take the list of lists variable called 'table'
        self.avTableRow(table)
        self.avTableColumn(table)

    def avTableRow(self, table):
        print("-----------------")
        print("2.1 Average of a table row excluding negative entries\n")

        A = table
        
        counter = 0

        for x in A:
            for y in x:
                if y < 0:
                    x.remove(y)

        listElems = [i for s in A for i in s if i>=1]
        rowLen = [len(x) for x in A]
        rowSum = [sum(b) for b in A]
        
        #print(listElems)
        #print(rowSum)
        #print(rowLen)

        sums = [x/y for x,y in zip(rowSum, rowLen)]
        for i in sums:
            print("The average of row %d is %f" % (counter + 1, i))
            counter += 1            

    def avTableColumn(self, table):
        print("-----------------")
        print("2.2 Average of a table column excluding negative entries\n")

        A = table

        print(A)
        
        for x in A:
            for y in range(len(x)):
                if x[y] < 0:
                    x[y] = 0

        for x in range(len(A)):
            print(str(A[x::3]).replace('[', '').replace(']', ''))
        
        counter = 0
        #print([len(col) for col in zip(*A)])
        averageColumn = [float(sum(col)) / len(col) for col in zip(*A)]

        for i in averageColumn:
            print("The average of column %d is %f" % (counter + 1, i))
            counter += 1
            
    def students(self):
        """Function holding the 3 lists (student names, module names
        and marks) for the other functions to call upon"""

        listOfStudents = ['John Smith', 'Tom Brown', 'Jason Bourne']
        modules = ['Physics', 'Mathematics', 'English', 'History']
        listofStudentMarks = [[79, 86, 89, 81],
                              [95, 95, 94, 93],
                              [71, 89, 97, 55]]

        self.avStudentMark(listOfStudents, listofStudentMarks)
        self.avModuleMark(modules, listofStudentMarks)
        self.studentReport(listOfStudents, listofStudentMarks)
        self.modulesReport(modules, listofStudentMarks)

    def avStudentMark(self, sList, sMarks):
        print("-----------------")
        print("2.3 Average mark for a student \n")

        # Using list comprehension to get average mark of each row
        averageStudentMarks = [float(sum(row)) / len(row) for row in sMarks]
        studentName = input(str("Please enter your full name: "))
        # Using list comprehension to turn all strings in list to lowercase
        studentList = [x.lower() for x in sList]
        # Initialising index variable to hold index of student names in list
        index = 0

        # Getting index of student name from user input
        for i in range(len(studentList)):
            if studentName == studentList[i]:
                index = i

        # Printing student name along with corresponding average mark
        if studentName.lower() in studentList:
            print('Student name: %s. Average for the registered modules: %f' % (studentName, averageStudentMarks[index]))
        else:
            print('There is no such student')

    def avModuleMark(self, modules, sMarks):
        print("-----------------")
        print("2.4 Average mark for a module \n")

        # Using list comprehension to get average mark of each column
        averageColumn = [float(sum(col)) / len(col) for col in zip(*sMarks)]
        moduleName = input(str("Please enter module name: "))
        # Using list comprehension to turn all strings in list to lowercase
        modName = [x.lower() for x in modules]

        # Initialising index variable to hold index of module names in list
        index = 0

        # Getting index of module name from user input
        for i in range(len(modName)):
            if moduleName == modName[i]:
                index = i

        if moduleName.lower() in modName:
            print('Module name: %s. Average for the registered modules: %f' % (moduleName, averageColumn[index]))
        else:
            print('There is no such Module')

    def studentReport(self, sList, sMarks):
        print("-----------------")
        print("2.5 Average mark for a module \n")

        averageStudentMarks = [float(sum(row)) / len(row) for row in sMarks]
        # zipping lists and reverse sorting based on the student marks to get it in descending order
        averageStudentMarks, sList = zip(*sorted(zip(averageStudentMarks, sList),reverse=True))

        for i in range(len(sList)):
            print('Student name: %s. Average for the registered modules: %f' % (sList[i], averageStudentMarks[i]))

    def modulesReport(self, modules, sMarks):
        print("-----------------")
        print("2.6 Average mark for a module \n")

        averageColumn = [float(sum(col)) / len(col) for col in zip(*sMarks)]
        averageColumn, modules = zip(*sorted(zip(averageColumn, modules), reverse=True))

        for i in range(len(modules)):
            print('Module name: %s. Average for the registered modules: %f' % (modules[i], averageColumn[i]))

    def main(self):
        #self.setLike()
        #self.sequenceLike()
        #self.consecutiveSequence()
        self.composingReports()
        self.students()
        

if __name__ == "__main__":
    Coursework = Coursework2()
    Coursework.main()
