import tkinter as tk
from PolyGalois2m import PolyGalois2m
from GUI import GUI

gui = GUI()

# to display final result
def updateResult(msg, r=0):
    if (len(msg) < 65):
        gui.FlabelD['text'] = (msg)
    else:
        gui.FlabelD['text'] = "Too large to display properly"

    dec = int(msg)
    finalsb = str(bin(dec))
    finalsh = str(hex(dec))
    if (len(finalsb) < 65):
        gui.FlabelB['text'] = (finalsb)
    else:
        gui.FlabelB['text'] = "Too large to display properly"

    gui.FlabelH['text'] = (finalsh)


def reduce(a, ir):
    al = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tt = ta.numPoly
    ttcho = tt.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))


def add(a, b, ir):
    al = []
    bl = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in b:
        bl.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tb = PolyGalois2m(bl, 0, ired)
    tt = ta + tb
    ttcho = tt.numPoly.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))


def sub(a, b, ir):
    al = []
    bl = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in b:
        bl.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tb = PolyGalois2m(bl, 0, ired)
    tt = ta.__sub__(tb)
    ttcho = tt.numPoly.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))


def mul(a, b, ir):
    al = []
    bl = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in b:
        bl.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tb = PolyGalois2m(bl, 0, ired)
    tt = ta.__mul__(tb)
    ttcho = tt.numPoly.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))


def div(a, b, ir):
    notdiv0 = 0
    for st in b:
        if (int(st) == 1):
            notdiv0 = 1
            break
    if (notdiv0 == 0):
        self.popupmsg("Can not divide by 0")

    al = []
    bl = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in b:
        bl.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tb = PolyGalois2m(bl, 0, ired)
    tt = ta.__floordiv__(tb)
    ttcho = tt.numPoly.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))


def inv(a, ir):
    al = []
    ired = []
    for st in a:
        al.append(int(st))
    for st in ir:
        ired.append(int(st))

    ta = PolyGalois2m(al, 0, ired)
    tt = ta.findInverse()
    ttcho = tt.coeffs
    dec = 0
    for i in range(len(ttcho)):
        degree = len(ttcho) - i - 1
        dec = dec + ttcho[i] * 2 ** degree
    updateResult(str(dec))
