from time import *
import random as  r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s, time_e, userInput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userInput)/ time_R
    return round(speed)
    

if __name__ == '__main__':
    while True:
        check=input("Ready to begin: yes or no :")
        if check=='yes':
            test = ["Typing speed also can be improved after checking it.", "who will give proper examples related to the speed.", "Make the best out of this tutorial and learn from our trainer","Welcome to my projects list"]
            test1 = r.choice(test)

            print("---===typing speed test===---")
            print(test1)
            print()
            print()

            time_1=time()
            testinput=input("Enter : ")
            time_2=time()

            print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")

            print('Error : ',mistake(test1,testinput))
        elif check=="no":
            print("Thanks you for using it!")
            break
        else:
            print("wrong input")
            break
