from random import randint
print("rock , paper , scissor")
cp = randint(0,3)
if cp == 0:
    Bot = "rock"
elif cp ==1:
    Bot = "paper"
else :
    Bot = "scissor"
ppl = input("player :")
if ppl == "Bot":
    print("Bot:",Bot)
    print("Tie")
elif ppl == "rock" :
    if Bot == "paper":
        print("Bot:",Bot)
        print("Bot win")
    else:
        print("Bot lose")
elif ppl=="scissor" :
    if Bot == "rock" :
        print("Bot: ",Bot)
        print("you lose")
    else:
        print("You Win")
elif player == "paper":
    if Bot == "scissors":
        print("Bot: ",Bot)
        print("You win")
    else:
        print("Bot: ",Bot)
        print("You Lose")
else:
    print("you move is not valid")
   
