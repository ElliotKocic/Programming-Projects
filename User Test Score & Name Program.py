# User Test Score & Name Program that connects to a mysql database inputting the data once recieved from the user
import os
import mysql.connector

while True:
        UserName = input("Please fill in your full name: ")
        if UserName.replace(" ", "").isalpha():
            break
        else:
            print("Please only enter letters for your name.")

def UserScore():
    while True:
        try:
            TestScore = input("Test Score out of 100: ")
            TestScore = int(TestScore)

            if int(TestScore) > 100 or int(TestScore) < 0:
                print("Please enter a value between 0-100.")
            else:
                break
        except:
            print("Please only enter numbers.")
    TestScorePercentage = round(((TestScore/100)*100), 1)
    return TestScorePercentage    
   
TestScore = 0


print("ICT:")
IctTestScore = UserScore()
print("Maths:")
MathsTestScore = UserScore()
print("Chemistry:")
ChemistryTestScore = UserScore()

print("Thank you for your entry " + UserName + ".")
print("ICT = " + str(IctTestScore) + "%" + ", Maths = " + str(MathsTestScore) + "%" + ", Chemistry = " + str(ChemistryTestScore) + "%")

SqlPassword = os.environ.get("MySql_Password")
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=SqlPassword,
    database="testscoresdb"
)

DBCursor = connection.cursor()

sql = "INSERT INTO studentTestScores (name, testScoreICT, testScoreMaths, testScoreChemistry) VALUES (%s, %s, %s, %s)"
val = (UserName, IctTestScore, MathsTestScore, ChemistryTestScore)
DBCursor.execute(sql, val)

connection.commit()
connection.close()
DBCursor.close()

