#Welcome message
from calendar import c


print(" ")
print("Welcome to Modulator")

#User input to choose module
moduleName = int(input("""WebDev(Enter 1)
Networking 3(Select 2)
Databases 1(Select 3)
OOP(Select 4)\n"""))
print(" ")

#Class for WebDev
class webDev:
    def __init__(self, test, project, exercises):
        self.test = test
        self.project = project
        self.exercises = exercises

    def overallWebGrade(self):
        webGrade = ((((self.test/30)*100) + ((self.project/40)*100) + ((self.exercises/30)*100)) / 3) 
        print("Your overall grade is ",webGrade,"%")

#If user selected WebDev
if moduleName == 1:
    print("Enter 'y' for grades you have\nEnter 'n' for grades you don't have.")
    webTest = input("Tests: ")
    project = input("Projects: ")
    exerTest = input("Exercises: ")

#When user has all grades
    if ((webTest == 'y') or (webTest == 'Y')) and ((project == 'y') or (project == 'Y')) and ((exerTest == 'y') or (exerTest == 'Y')):
        testGrade = float(input("Enter your test grade(%): "))
        
        #To cap test grade at 30
        while ((testGrade < 0) or (testGrade > 30)):
            testGrade = float(input("Test grade is only marked over 30\nPlease type in a valid grade:\n"))
    
        projectGrade = float(input("Enter your project grade(%): "))
        #To cap project grade at 40
        while ((projectGrade < 0) or (projectGrade > 40)):
            projectGrade = float(input("Project grade is only marked over 40\nPlease type in a valid grade:\n"))


        exercisesGrade = float(input("Enter the grade for your exercises(%): "))
        #To cap exercises grade at 30
        while ((exercisesGrade < 0) or (exercisesGrade > 30)):
            exercisesGrade = float(input("The grade for exercises is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(testGrade, projectGrade, exercisesGrade)
        Calc1.overallWebGrade()

    #When user has both test grade and exercise grade
    elif ((webTest == 'y') or (webTest == 'Y')) and ((project == 'n') or (project == 'N')) and ((exerTest == 'y') or (exerTest == 'Y')):
        testGrade = float(input("Enter your test grade(%): "))
        
        #To cap test grade at 30
        while ((testGrade < 0) or (testGrade > 30)):
            testGrade = float(input("Test grade is only marked over 30\nPlease type in a valid grade:\n"))

        exercisesGrade = float(input("Enter the grade for your exercises(%): "))
        #To cap exercises grade at 30
        while ((exercisesGrade < 0) or (exercisesGrade > 30)):
            exercisesGrade = float(input("The grade for exercises is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(testGrade, 0 , exercisesGrade)
        Calc1.overallWebGrade()

    #When user has both test grade and project grade
    elif ((webTest == 'y') or (webTest == 'Y')) and ((project == 'y') or (project == 'Y')) and ((exerTest == 'n') or (exerTest == 'N')):
        testGrade = float(input("Enter your test grade(%): "))
        
        #To cap test grade at 30
        while ((testGrade < 0) or (testGrade > 30)):
            testGrade = float(input("Test grade is only marked over 30\nPlease type in a valid grade:\n"))
    
        projectGrade = float(input("Enter your project grade(%): "))
        #To cap project grade at 40
        while ((projectGrade < 0) or (projectGrade > 40)):
            projectGrade = float(input("Project grade is only marked over 40\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(testGrade, projectGrade, 0)
        Calc1.overallWebGrade()

    #When user has both project grade and exercise grade
    elif ((webTest == 'n') or (webTest == 'N')) and ((project == 'y') or (project == 'Y')) and ((exerTest == 'y') or (exerTest == 'Y')):
        projectGrade = float(input("Enter your project grade(%): "))
        #To cap project grade at 40
        while ((projectGrade < 0) or (projectGrade > 40)):
            projectGrade = float(input("Project grade is only marked over 40\nPlease type in a valid grade:\n"))


        exercisesGrade = float(input("Enter the grade for your exercises(%): "))
        #To cap exercises grade at 30
        while ((exercisesGrade < 0) or (exercisesGrade > 30)):
            exercisesGrade = float(input("The grade for exercises is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(0, projectGrade, exercisesGrade)
        Calc1.overallWebGrade()

    #When user has only webtest grade
    elif ((webTest == 'y') or (webTest == 'Y')) and ((project == 'n') or (project == 'N')) and ((exerTest == 'n') or (exerTest == 'N')):
        testGrade = float(input("Enter your test grade(%): "))

        #To cap test grade at 30
        while ((testGrade < 0) or (testGrade > 30)):
            testGrade = float(input("Test grade is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(testGrade, 0, 0)
        Calc1.overallWebGrade()

    #When user has only project grade
    elif ((webTest == 'n') or (webTest == 'N')) and ((project == 'y') or (project == 'Y')) and ((exerTest == 'n') or (exerTest == 'N')):
        projectGrade = float(input("Enter your project grade(%): "))

        #To cap project grade at 40
        while ((projectGrade < 0) or (projectGrade > 40)):
            projectGrade = float(input("Project grade is only marked over 40\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(0, projectGrade, 0)
        Calc1.overallWebGrade()

    #When user has only exercise grade
    elif ((webTest == 'n') or (webTest == 'N')) and ((project == 'n') or (project == 'N')) and ((exerTest == 'y') or (exerTest == 'Y')):
        exercisesGrade = float(input("Enter the grade for your exercises(%): "))

        #To cap exercises grade at 30
        while ((exercisesGrade < 0) or (exercisesGrade > 30)):
            exercisesGrade = float(input("The grade for exercises is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc1 = webDev(0, 0, exercisesGrade)
        Calc1.overallWebGrade()
    else:
        pass


#class for Networking 3
class networking:
    def __init__(self,exam,quiz1,quiz2,practicalTest,caWork):
        self.exam = exam
        self.quiz1 = quiz1
        self.quiz2 = quiz2
        self.practicalTest = practicalTest
        self.caWork = caWork

    def overallNetworkingGrade(self):
        networkingGrade = ((((self.exam/50) * 100) + ((self.quiz1/5) * 100) + ((self.quiz2/5) * 100) + ((self.practicalTest/10) * 100) + ((self.caWork/30) * 100)) / 5)
        print("Your overall grade is ",networkingGrade,"%")

#If user selected networking
if moduleName == 2:
    print("Enter 'y' for grades you have\nEnter 'n' for grades you don't have.")
    exam = input("Exam: ")
    quiz1 = input("Quiz 1: ")
    quiz2 = input("Quiz 2: ")
    practicalTest = input("Practical Test: ")
    caWork = input("CA Work: ")

#When user has all grades
    if ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    
        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))


        quiz2Grade = float(input("Enter your Quiz 2 grade(%): "))
        #To cap quiz 2 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        
        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        
        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))


        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, quiz2Grade, practicalTestGrade, caWorkGrade)
        Calc2.overallNetworkingGrade()

    #When user has every grade but the exam
    elif ((exam == 'n') or (exam == 'N')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'y') or (caWork == 'Y')):
        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))


        quiz2Grade = float(input("Enter your Quiz 2 grade(%): "))
        #To cap quiz 2 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        
        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        
        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))


        #Prints final grade
        Calc2 = networking(0, quiz1, quiz2, practicalTest, caWork)
        Calc2.overallNetworkingGrade()

    #When user has every grade but Quiz 1
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'n') or (quiz1 == 'N')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz2Grade = float(input("Enter your Quiz 2 grade(%): "))
        #To cap quiz 2 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        
        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        
        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))

        
        #Prints final grade
        Calc2 = networking(examGrade, 0, quiz2Grade, practicalTestGrade, caWorkGrade)
        Calc2.overallNetworkingGrade()


    #When user has every grade but Quiz 2
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'n') or (quiz2 == 'N')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        
        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        
        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))

        
        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, 0, practicalTestGrade, caWorkGrade)
        Calc2.overallNetworkingGrade()


        #When user has every grade but practical test
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'n') or (practicalTest == 'N')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))


        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))

        
        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, quiz2Grade, 0, caWorkGrade)
        Calc2.overallNetworkingGrade()


    #When user has every grade but CA work
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'n') or (caWork == 'N')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, quiz2Grade, practicalTestGrade, 0)
        Calc2.overallNetworkingGrade()
    
       #When user has every grade but CA work and practical test
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'n') or (practicalTest == 'N')) and ((caWork == 'n') or (caWork == 'N')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, quiz2Grade, 0, 0)
        Calc2.overallNetworkingGrade()

       #When user has every grade but CA work and quiz 2
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'n') or (quiz2 == 'N')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'n') or (caWork == 'N')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    
        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, 0, practicalTestGrade, 0)
        Calc2.overallNetworkingGrade()

       #When user has every grade but CA  and quiz 1 work
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'n') or (quiz1 == 'N')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'n') or (caWork == 'N')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
    

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, 0, quiz2Grade, practicalTestGrade, 0)
        Calc2.overallNetworkingGrade()

       #When user has every grade but CA work and exam
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'n') or (caWork == 'N')):

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(0, quiz1Grade, quiz2Grade, practicalTestGrade, 0)
        Calc2.overallNetworkingGrade()

    #When user has every grade but quiz 1 and quiz 2
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'n') or (quiz1 == 'N')) and ((quiz2 == 'n') or (quiz2 == 'N')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

    
        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, 0, 0, practicalTestGrade, caWorkGrade)
        Calc2.overallNetworkingGrade()

    
    #When user has every grade but quiz 1 and practical test
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'n') or (quiz1 == 'N')) and ((quiz2 == 'y') or (quiz2 == 'Y')) and ((practicalTest == 'n') or (practicalTest == 'N')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        quiz2Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz2Grade < 0) or (quiz2Grade > 5)):
            quiz2Grade = float(input("Quiz 2 grade is only marked over 5\nPlease type in a valid grade:\n"))

        caWorkGrade = float(input("Enter your CA Work test grade(%): "))
        #To cap  test grade at 30
        while ((caWorkGrade < 0) or (caWorkGrade > 30)):
            caWorkGrade = float(input("CA Work grade is only marked over 30\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, 0, quiz2, 0, caWorkGrade)
        Calc2.overallNetworkingGrade()

      #When user has every grade but quiz 2 and CA work
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'n') or (quiz2 == 'N')) and ((practicalTest == 'y') or (practicalTest == 'Y')) and ((caWork == 'n') or (caWork == 'N')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, 0, practicalTestGrade, 0)
        Calc2.overallNetworkingGrade()

     #When user has every grade but quiz 2 and practical test
    elif ((exam == 'y') or (exam == 'Y')) and ((quiz1 == 'y') or (quiz1 == 'Y')) and ((quiz2 == 'n') or (quiz2 == 'N')) and ((practicalTest == 'n') or (practicalTest == 'N')) and ((caWork == 'y') or (caWork == 'Y')):
        
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap exam grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        quiz1Grade = float(input("Enter your Quiz 1 grade(%): "))
        #To cap quiz 1 grade at 5
        while ((quiz1Grade < 0) or (quiz1Grade > 5)):
            quiz1Grade = float(input("Quiz 1 grade is only marked over 5\nPlease type in a valid grade:\n"))

        practicalTestGrade = float(input("Enter your practical test grade(%): "))
        #To cap practical test grade at 10
        while ((practicalTestGrade < 0) or (practicalTestGrade > 10)):
            practicalTestGrade = float(input("Practical Test grade is only marked over 10\nPlease type in a valid grade:\n"))
            
        #Prints final grade
        Calc2 = networking(examGrade, quiz1Grade, 0, 0, caWork)
        Calc2.overallNetworkingGrade()


    else:
        pass


#Class for databases
class databases:
    def __init__(self, ca, exam):
        self.ca = ca
        self.exam = exam

    def overallDatabasesGrade(self):
        databasesGrade = ((((self.ca/50)*100) + ((self.exam/50)*100)) / 2) 
        print("Your overall grade is ",databasesGrade,"%")

#If user selected databases 
if moduleName == 3:
    print("Enter 'y' for grades you have\nEnter 'n' for grades you don't have.")
    ca = input("CA: ")
    exam = input("Exam: ")

    #When user has both grades
    if ((ca == 'y') or (ca == 'Y')) and ((exam == 'y') or (exam == 'Y')):
        caGrade = float(input("Enter your CA grade(%): "))
        
        #To cap test grade at 50
        while ((caGrade < 0) or (caGrade > 50)):
            caGrade = float(input("Test grade is only marked over 50\nPlease type in a valid grade:\n"))
    
        examGrade = float(input("Enter your exam grade(%): "))
        #To cap project grade at 50
        while ((examGrade < 0) or (examGrade > 40)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc3 = databases(caGrade, examGrade)
        Calc3.overallDatabasesGrade()

    #When user only has CA
    elif ((ca == 'y') or (ca == 'Y')) and ((exam == 'n') or (exam == 'N')):
        caGrade = float(input("Enter your CA grade(%): "))
        
        #To cap test grade at 50
        while ((caGrade < 0) or (caGrade > 50)):
            caGrade = float(input("Test grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc3 = databases(caGrade, 0)
        Calc3.overallDatabasesGrade()

    #When user only has exam
    elif ((ca == 'n') or (ca == 'N')) and ((exam == 'y') or (exam == 'Y')):
        examGrade = float(input("Enter your exam grade(%): "))
        
        #To cap test grade at 50
        while ((examGrade < 0) or (examGrade > 50)):
            examGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc3 = databases(0, examGrade)
        Calc3.overallDatabasesGrade()
    else:
        pass

class OOP:
    def __init__(self, labs, assignment, exam):
        self.labs = labs
        self.assignment = assignment
        self.exam = exam

    def overallOOPGrade(self):
        oopGrade = (((((self.labs/40) + (self.assignment/60) * 100))) + (((self.exam/50)*100)) / 2) 
        print("Your overall grade is ",oopGrade,"%")

#If user selected OOP
if moduleName == 4:
    print("Enter 'y' for grades you have\nEnter 'n' for grades you don't have.")
    labs = input("Labs: ")
    assignment = input("Assignment: ")
    examOOP = input("Exam: ")

    #When user has all grades
    if ((labs == 'y') or (labs == 'Y')) and ((assignment == 'y') or (assignment == 'Y')) and ((examOOP == 'y') or (examOOP == 'Y')):
        
        labGrade = float(input("Enter your lab grade(%): "))
        #To cap lab grade at 40
        while ((labGrade < 0) or (caGrade > 40)):
            labGrade = float(input("Lab grade is only marked over 40\nPlease type in a valid grade:\n"))
    
        assignmentGrade = float(input("Enter your assignment grade(%): "))
        #To cap project grade at 60
        while ((assignmentGrade < 0) or (assignmentGrade > 60)):
            assignmentGrade = float(input("Exam grade is only marked over 60\nPlease type in a valid grade:\n"))

        examOOPGrade = float(input("Enter your OOP grade(%): "))
        #To cap exam grade at 50
        while ((examOOPGrade < 0) or (examOOPGrade > 50)):
            assignmentGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(labGrade, assignmentGrade, examOOPGrade)
        Calc4.overallOOPGrade()

    #When user has only lab grade
    elif ((labs == 'y') or (labs == 'Y')) and ((assignment == 'n') or (assignment == 'N')) and ((examOOP == 'n') or (examOOP == 'N')):
        
        labGrade = float(input("Enter your lab grade(%): "))
        #To cap lab grade at 40
        while ((labGrade < 0) or (caGrade > 40)):
            labGrade = float(input("Lab grade is only marked over 40\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(labGrade, 0, 0)
        Calc4.overallOOPGrade()

    #When user has only lab and assignment grade
    elif ((labs == 'y') or (labs == 'Y')) and ((assignment == 'y') or (assignment == 'Y')) and ((examOOP == 'n') or (examOOP == 'N')):
        
        labGrade = float(input("Enter your lab grade(%): "))
        #To cap lab grade at 40
        while ((labGrade < 0) or (caGrade > 40)):
            labGrade = float(input("Lab grade is only marked over 40\nPlease type in a valid grade:\n"))

        assignmentGrade = float(input("Enter your assignment grade(%): "))
        #To cap project grade at 60
        while ((assignmentGrade < 0) or (assignmentGrade > 60)):
            assignmentGrade = float(input("Exam grade is only marked over 60\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(labGrade, assignmentGrade, 0)
        Calc4.overallOOPGrade()

    #When user has only assignment grade
    elif ((labs == 'n') or (labs == 'N')) and ((assignment == 'y') or (assignment == 'Y')) and ((examOOP == 'n') or (examOOP == 'N')):
        
        assignmentGrade = float(input("Enter your assignment grade(%): "))
        #To cap project grade at 60
        while ((assignmentGrade < 0) or (assignmentGrade > 60)):
            assignmentGrade = float(input("Exam grade is only marked over 60\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(0, assignmentGrade, 0)
        Calc4.overallOOPGrade()

       #When user has only exam grade
    elif ((labs == 'n') or (labs == 'N')) and ((assignment == 'n') or (assignment == 'N')) and ((examOOP == 'y') or (examOOP == 'Y')):
        
        examOOPGrade = float(input("Enter your OOP grade(%): "))
        #To cap exam grade at 50
        while ((examOOPGrade < 0) or (examOOPGrade > 50)):
            assignmentGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))
        
        #Prints final grade
        Calc4 = OOP(0, 0, examOOPGrade)
        Calc4.overallOOPGrade()

    #When user has only lab and exam grades
    elif ((labs == 'y') or (labs == 'Y')) and ((assignment == 'n') or (assignment == 'N')) and ((examOOP == 'y') or (examOOP == 'Y')):
        
        labGrade = float(input("Enter your lab grade(%): "))
        #To cap lab grade at 40
        while ((labGrade < 0) or (caGrade > 40)):
            labGrade = float(input("Lab grade is only marked over 40\nPlease type in a valid grade:\n"))

        examOOPGrade = float(input("Enter your OOP grade(%): "))
        #To cap exam grade at 50
        while ((examOOPGrade < 0) or (examOOPGrade > 50)):
            assignmentGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(labGrade, 0, examOOPGrade)
        Calc4.overallOOPGrade()

    #When user has all grades
    elif ((labs == 'n') or (labs == 'N')) and ((assignment == 'y') or (assignment == 'Y')) and ((examOOP == 'y') or (examOOP == 'Y')):
        
        assignmentGrade = float(input("Enter your assignment grade(%): "))
        #To cap project grade at 60
        while ((assignmentGrade < 0) or (assignmentGrade > 60)):
            assignmentGrade = float(input("Exam grade is only marked over 60\nPlease type in a valid grade:\n"))

        examOOPGrade = float(input("Enter your OOP grade(%): "))
        #To cap exam grade at 50
        while ((examOOPGrade < 0) or (examOOPGrade > 50)):
            assignmentGrade = float(input("Exam grade is only marked over 50\nPlease type in a valid grade:\n"))

        #Prints final grade
        Calc4 = OOP(0, assignmentGrade, examOOPGrade)
        Calc4.overallOOPGrade()
    else:
        pass



    


    




