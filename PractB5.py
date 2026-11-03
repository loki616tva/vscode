low = 1
high = 100

print("think of a number in 1 to 100")
user_input=input("ready with the number? (yes/no): ").lower()

if user_input=="yes":
    while low<=high:
        guess = (low+high)//2
        print("your number is: ", guess)

        feedback = input("tell me higher,lower or correct: ").lower()

        if feedback=="correct":
            print("i guessed your number")
            break
        elif feedback=="lower":
            high=guess-1
        elif feedback=="higher":
            low=guess+1

        else:
            print("please enter higher, lower or correct")
