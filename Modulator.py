#Welcome message
from calendar import c


print(" ")
print("Welcome to Modulator")

#User input to choose module
moduleName = int(input("""WebDev(Enter 1)
Networking 3(Select 2)
Databases 1(Select 3)
Networking Programming(Select 4)
Databases(Select 5)\n"""))
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
    else:
        pass






