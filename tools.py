def isBin(st):
    return bool(st) and set(st).issubset({'0', '1'})


def isHex(st):
    st = st.lower()
    return bool(st) and set(st).issubset(
        {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'})


def binListToDec(lista):
    dec = 0
    for i in range(len(lista)):
        degree = len(lista) - i - 1
        dec = dec + lista[i] * 2 ** degree
    return dec


def charListToIntList(charList):
    print(charList)
    for i in range(len(charList)):
        charList[i] = int(charList[i])
    return charList


def hexToBin(hex):
    dec = int(hex, 16)
    binary = bin(dec)
    st = str(binary)
    temp = list(st[2:])
    return temp

def stringifyBinList(lista):
    st = ""
    for i in range(len(lista)):
        if lista[i] == 1:
            degree = len(lista) - i - 1
            st += "x^" + str(degree) + " + "
    return st[:-2]