import random  # import random library.


read_num = input("Type a number: ") # take an input from user to get the range where randow functions.

guesses = 0

if read_num.isdigit(): # isdigit() check that the  value which is taken by user is in digit or int format or not.
    read_num = int(read_num)  #converting the user input to int format.

    if read_num <= 0:  #This condition is applied because this game is schedule for only natural number.
        print("please type a number larger than 0 next time. ")
        quit()
    
else:
    print("please type a number next time. ")
    quit()

random_number = random.randint(0, read_num) #intialize the random guess by system which range provided by the user, and function used is randint and randrange.


while True:  # while true the above condtion then this loop will work and comapre that the user guess is == system number

    guesses += 1  #counting the number of guesses user made for correct guess
    user_guess = input("Make a guess ")  # Take user_guess input

    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("please type a number next time. ")
        continue

    if user_guess == random_number:
        print("You got it ! ")
        break
    
    else:
        print("You got it wrong! ")

print("You got it in" , guesses , "guessses") 




    
    






