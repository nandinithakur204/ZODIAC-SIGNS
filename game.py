import random
name = random.randrange(1,4)

temp = ''

if name == 1 :

    temp = 'rock'

elif name == 2 :

    temp = 'paper'

elif name == 3:

    temp = 'sissor'

x = 1  

while x == 1 :

    move = input("enter your move")

    if move == 'rock' and temp == 'sissor' :

        print('user win')

    elif move == 'paper' and temp == 'rock' :

        print('user win')  

    elif move == 'sissor' and temp == 'paper' :

        print('user win')
  
    else :

        print('system win') 

    x = int(input('Press 0 for exit and press 1 for continue'))  

    if x==0:
           
         break



            
        
          
