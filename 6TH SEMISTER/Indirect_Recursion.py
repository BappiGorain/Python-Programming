def funA(x):
    if x > 0:
        print(f"funA:{x}")
        funB(x-1)

def funB(x):
    if x > 0:
        print(f"funB:{x}")
        funA(x-1)


funA(5)

