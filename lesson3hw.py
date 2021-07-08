import random
x=0
number=random.randint(1,20)
print('Do you want to play a game?')

while x < 6:
    print('Guess a number,1~20')
    guess = int(input())
    
    x = x+1
    
    if guess < number:
        print('Your guess is too small!')
        
    if guess > number:
        print('your number is too big!')
        
    if guess == number:
        break
    
if guess == number:
    print("You're right! You guess it with", str(x), "guesses!")
if x == 5:
    print('You lose! The number is', str(number))       

   
