import mysql.connector as connector
import time
import os

class QuizGame:
    def __init__(self):
        self.config = {
        'user':'root',
        'password':'sahilkhan@7824',
        'host':'localhost',
        'database':'quizgame'
        }   


    def quiz(self, username):
        os.system('cls')
        print("="*120)
        print(" WELCOME TO THE QUIZ GAME ".center(120, '-'))
        print("="*120)
        choice = input("Do you want to play the quiz game? (yes/no): ")
        while choice != 'no' or choice != 'n':
            if choice == 'no':
                print("Thank you for playing the quiz game.")
                time.sleep(3)
                exit()
            score = 0
            connection = connector.connect(**self.config)
            cursor = connection.cursor()
            
            # Randomly selecting 10 questions from the quizdata table
            cursor.execute("SELECT * FROM quizdata ORDER BY RAND() LIMIT 10")
            result = cursor.fetchall()
            
            print("-"*120)
            print(" ANSWER THE FOLLOWING QUESTIONS ".center(120))
            print("-"*120)
            for i in range(10):
                print("Question",i+1)
                print(result[i][1])
                print("A.",result[i][2])
                print("B.",result[i][3])
                print("C.",result[i][4])
                print("D.",result[i][5], end='\n\n')
                answer = input("Enter your answer: ")
                
                print("-"*120)
                if answer.upper() == result[i][6]:
                    score += 1
                    print("Correct answer.")
                else:
                    print("Incorrect answer.")
                    print("Correct answer is:",result[i][6])
                print("-"*120)
                    
                    
                
            print("Your score is:",score)
            
            # writing the score into the user_info table
            cursor.execute("UPDATE user_info SET score = %s WHERE username = %s",(score,username))
            connection.commit()
            cursor.close()
            choice = input("Do you want to play the quiz game? (yes/no): ")
            
        

    def login(self):
        os.system('cls')
        print("="*120)
        print(" LOGIN TO THE SYSTEM ".center(120, '-'))
        print("="*120)
        connection = connector.connect(**self.config)
        cursor = connection.cursor()
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        cursor.execute("SELECT * FROM user_info WHERE username = %s AND password = %s",(username, password))
        result = cursor.fetchall()
        
        if len(result) == 0:
            print("Invalid username or password. Please try again.")
            login = input("Do you want to login again? (yes/no): ")
            if login == 'yes':
                self.login()
            else:
                print("Thank you for using the quiz game.")
                time.sleep(3)
                os.system('cls')
        else:
            print("You have successfully logged in.")
            print("Bringing you to the quiz page...")
            time.sleep(3)
            os.system('cls')
        
        cursor.close()
        self.quiz(username)
        

    def signup(self):
        os.system('cls')
        print("="*120)
        print(" CREATE YOUR ACCOUNT ".center(120, '-'))
        print("="*120)
        connection = connector.connect(**self.config)
        cursor = connection.cursor()
        
        fullname = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter you phone no.: ")
        flag = True
        while flag:
            
            username = input("Create your username: ")
            # cheching if username already exists in the user table
            cursor.execute("SELECT * FROM user_info WHERE username = %s",(username,))
            result = cursor.fetchall()
            if len(result) == 0:
                flag = False
            else:
                print("Username already exists. Please try again.")
            
        password = input("Create your password: ")
        
        cursor.execute("INSERT INTO user_info (fullname, phone, email, username, password) VALUES (%s, %s, %s, %s, %s)",(fullname, phone, email, username, password))    
        
        connection.commit()
        cursor.close()
        print("You have successfully signed up.")
        print("Bringing you to the login page...")
        time.sleep(3)
        os.system('cls')
        self.quiz(username)        
        
def main():
    game = QuizGame()
    print("="*120)
    print(" WELCOME TO THE QUIZ GAME ".center(120, '-'))
    print("="*120)
    print("1. Login")
    print("2. Signup")
    print("0. Exit")
    print("-"*120)
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            game.login()
        case 2:
            game.signup()
        case 0:
            print("Thank you for using the quiz game.")
            time.sleep(3)
            os.system('cls')
            exit()
            
if __name__ == '__main__':
    main()