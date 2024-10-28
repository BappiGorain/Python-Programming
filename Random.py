import random


f1,f2,f3,f4,f5,f6 = 0,0,0,0,0,0

for roll in range(60000):
    num = random.randrange(1,7)
    if num == 1:
        f1+=1
    if num == 2:
        f2+=1
    if num == 3:
        f3+=1
    if num == 4:
        f4+=1
    if num == 5:
        f5+=1
    if num == 6:
        f6+=1
        

print(f"{1 :> 4} {f1 :> 13}")
print(f"{2 :> 4} {f2 :> 13}")
print(f"{3 :> 4} {f3 :> 13}")
print(f"{4 :> 4} {f4 :> 13}")
print(f"{5 :> 4} {f5 :> 13}")
print(f"{6 :> 4} {f6 :> 13}")
