# turtle race game
import turtle as t1
import random
t1.pen(pensize=5,speed=0)
t1.color("red")
t1.shape("turtle")
t1.penup()
t1.goto(-275,100)
#t1.pendown()
t2=t1.clone()
t2.color("green")
t2.penup()
t2.goto(-275,-100)
#t2.pendown()
t1.goto(275,60)
t1.pendown()
t1.circle(40)
t1.penup()
t1.goto(-275,100)
t1.pendown()
t2.goto(275,-140)
t2.pendown()
t2.circle(40)
t2.penup()
t2.goto(-275,-100)
t2.pendown()
dice=[1,2,3,4,5,6]
for i in range(25):
    if t1.pos() >= (275,100):
        print("Player 1 won!!!")
        break
    elif t2.pos() >= (275,-100):
        print("Player 2 won!!!")
        break
    else:
        t1_turn = input("---------------------------------------------\nPlayer1 : Press Enter to roll the dice :")
        dice_result = random.choice(dice)
        print(f"The result of the dice is {dice_result}")
        print(f"Movement : {dice_result*10}")
        t1.fd(dice_result*10)
        t2_turn = input("---------------------------------------------\nPlayer2 : Press Enter to roll the dice :")
        dice_result = random.choice(dice)
        print(f"The result of the dice is {dice_result}")
        print(f"Movement : {dice_result*10}")
        t2.fd(dice_result*10)
t1.done()