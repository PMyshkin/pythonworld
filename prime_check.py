#*Author : Prince.Myshkin

#*"You should pass us by and forgive us our happiness," said the prince in a low voice!!!"
#*“Beauty will save the world"!!

########################################################################################################
#Hey!
Number = int(input())
a=2
Prime=2
while a < Number -1:
    if Number % a == 0:
        print(False)
        break
    a += 1
    Prime +=1
    if Prime == Number -1:
        print(True)



