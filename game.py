import random
winning_num=random.randint(1,100)
guess=1
lucky_num=int(input("Enter your lucky number b/w 1 to 100: "))
game_over=False

while not game_over:
   
    if winning_num==lucky_num:
         print("Congratulations, you won and your attempt is {guess}")
         game_over=True
    else:
         if lucky_num < winning_num:
             print("low guess")
         else :
             print("high guess") 


         guess+=1
         lucky_num=int(input("Enter your lucky number b/w 1 to 100: "))  

# winning_num=85
# lucky_num=int(input("Enter your lucky number b/w 1 to 100: "))
# guess=1
# game_over=False


# while not game_over:
#     if winning_num==lucky_num:
#         print(f"Congratulations, you won and you attempt is {guess}")
#         game_over=True
#     else:
#         if lucky_num < winning_num:
#             print("low guess")
#         else :
#             print("high guess") 


#         guess+=1
#         lucky_num=int(input("Enter your lucky number b/w 1 to 100: "))  
        




