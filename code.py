class Student:
  def __init__(self, data):
    self.regNum = data[0]
    self.name = data[1]
    self.branch = data[2]
    self.phoneNum = data[3]
  
  def getData(data):
    return (data.regNum, data.name, data.branch, data.phoneNum)

def writeDataTofile(studentData):
  new_file_content = ""
  reading_file = open("input.txt", "r")
  for line in reading_file:
    stripped_line = line.strip()
    regNum = int(line.split(" ")[0])
    studentObject = studentData[regNum]
    replaceString = " ".join(list(studentObject.getData()))
    new_line = stripped_line.replace(stripped_line, replaceString.strip())
    new_file_content += new_line + "\n"
  reading_file.close()

  writing_file = open("input.txt", "w")
  writing_file.write(new_file_content)
  writing_file.close()
  

# This method handles user request and provides the required information
def handleUserRequest(n, studentsData):
    if n != 1 and n != 2:
        print("Invalid request")
        return
    index = -1
    print("Enter student register number")
    regNum = int(input())
    if regNum not in studentsData:
        print("Register number not found")
        return
    if n == 1:
        print(Student.getData(studentsData[regNum]))
    else:
        print("select the field you want to change\n1. Name\n2. phone Number\n3. Branch")
        selectedValue = int(input())
        if selectedValue == 1:
            print("Enter name")
            name = input()
            studentsData[regNum].name = name
        elif selectedValue == 2:
            print("Enter Phone Number to update")
            phoneNum = input()
            studentsData[regNum].phoneNum = phoneNum
        elif selectedValue == 3:
            print("Enter branch to update")
            branch = input()
            studentsData[regNum].branch = branch
        else:
            print("Invalid request")
            return
        
# main method holds input dataset        
def main():
    print("Welcome to Student Portal\nSelect your request")
    inputData = open("input.txt", "r")
    studentsData = dict()
    for entry in inputData:
      eachStudent = entry.split(" ")
      regNum = int(eachStudent[0])
      studentsData[regNum] = Student(eachStudent)
    while(1):
        print("Enter 1 to display data\nEnter 2 to update data")
        n = int(input())
        handleUserRequest(n, studentsData)
        print("press y to continue or n to exit")
        flowPoint = input()
        if flowPoint == 'n':
            print("Thanks for using student Portal")
            break
    writeDataTofile(studentsData)
#method call to trigger the flow            
main()
