def isBin(st):
    """
    Checks if st is a valid binary number in a string format
    :param st: string to check
    :return: bool
    """
    return bool(st) and set(st).issubset({'0', '1'})


def isHex(st):
    """
    Checks if st is a valid hexadecimal number in a string format
    :param st: string to check
    :return: bool
    """
    st = st.lower()
    return bool(st) and set(st).issubset(
        {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'})


def binListToDec(lista):
    """
    Considers lista as a list of coefficients for a binary polynomial,
    calculate the decimal representation of that polynomial and returns it
    :param lista:
    :return: int
    """
    dec = 0
    for i in range(len(lista)):
        degree = len(lista) - i - 1
        dec = dec + lista[i] * 2 ** degree
    return dec


def charListToIntList(charList):
    """
    Converts all the elements of charList from string to int
    :param charList:
    :return: modified charList
    """
    for i in range(len(charList)):
        charList[i] = int(charList[i])
    return charList


def hexToBin(hexNum):
    """
    Converts hex to bin
    :param hexNum: string
    :return: bin string
    """
    dec = int(hexNum, 16)
    binary = bin(dec)
    st = str(binary)
    temp = list(st[2:])
    return temp


def stringifyBinList(lista):
    """
    Considers lista as a list of coefficients of a binary polynomial.
    :param lista:
    :return: An appropriate string representation of lista
    """
    st = ""
    for i in range(len(lista)):
        if lista[i] == 1:
            degree = len(lista) - i - 1
            st += "x^" + str(degree) + " + "
    return st[:-2]
