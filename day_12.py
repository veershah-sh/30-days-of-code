class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
      self.firstName = firstName
      self.lastName = lastName
      self.idNumber = idNumber
      self.scores = scores

    def calculate(self):
      sum = 0 
      size = len(self.scores)
      for i in self.scores:
         sum += i
      grade = sum / size

      if(grade >= 90 and grade <= 100):
         grade = 'O'
      elif(grade >= 80 and grade < 90):
         grade = 'E'
      elif(grade >= 70 and grade < 80):
         grade = 'A'
      elif(grade >= 55 and grade < 70):
         grade = 'P'
      elif(grade >= 40 and grade < 55):
         grade = 'D'
      else:
         grade = 'T'
      return grade


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())