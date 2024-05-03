class person:
    def __init__(self, name , age, cid):
        #assinign attributes
        self.name = name
        self.age = age
        self.cid = cid

        #definign bheaviour/methods
    def walk(self):
            print(self.name, 'is walking')

    def talk(self):
            print (self.name, 'is talking')
        
    def sleep(self):
            print (self.name, 'is SLEPPING')
        
    def eAT(self):
            print (self.name, 'is eating')
    
class teacher(person):
    def __init__(self, name, age, cid, subject, salary,department, designation):
          super().__init__(name,age,cid)
          self.subject = subject
          self.salary = salary
          self.department = department
          self.desiganation = designation

    def teach(self):
          print(self.namem, "is teaching")


    
    def student_grade(self):
          print(self.namem, "is grading")

    
    def attend_meeting(self):
          print(self.namem, "is attending meeting")


class student (person):
      def __init__(self, name, age, cid, std_id, course, year, gpa):
            super().__init__(name, age, cid)
            self.std_id = std_id
            self.course = course
            self.year = year
            self.gpa = gpa
        #bheaviour
      def study(self):
            print (self.name, "is studying")
        
      def attend_calss(self):
            print (self.name, "is attending calss")

    

      def writ_exam(self):
        
            print (self.name, "is is writing exam")
t1 = teacher("tashi",30,12345,"accounts",30000,"commerce", 'assistant')
t2 = teacher("dorji",20,1245,"bio",3000,"math", 'health codinator')

s1 = student ('wangchuk', 17, 12008001717, 555555, ' bbib', 2023, 5)
s2 = student ('penjor', 18, 12888001717, 5555, ' bbiA', 2024, 2)

if s1.gpa >s2.gpa:
      print (s1.name ,'is better than', s2.name )
      student_information = 'year:'+ str(s2.year) + 'course' + s2.course
      print (student_information)
else:
      print (s2.name ,'is better than', s1.name )
      student_information = 'year:'+ str(s1.year) + 'course' + s1.course
      print (student_information)
      

student_storage = [s1, s2]


for std in student_storage:
      print(std.name)
      print(std.gpa)
      print(std.course)
      print("========")
      



        









        
        
       
        


       
      

        
    


        