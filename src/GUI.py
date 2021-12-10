import tkinter as tk
from tkinter import RIGHT, Y, END

import tools


class GUI:
    myConnector = None

    def __init__(self, gui):
        """
        Instantiates the main GUI, and returns the self to Launcher for linking to backend
        :param gui: Empty list used to return self
        """
        gui.append(self)
        master = tk.Tk()
        master.wm_title("Galois Polynomials Calculator")
        master.geometry("1200x500")

        tk.Label(master, text="Polynomial1 in binary").grid(row=0, column=1, ipadx=200)
        tk.Label(master, text="Polynomial2 in binary").grid(row=1, column=1, ipadx=200)
        tk.Label(master, text="Polynomial1 in HEX").grid(row=2, column=1, ipadx=200)
        tk.Label(master, text="Polynomial2 in HEX").grid(row=3, column=1, ipadx=200)
        tk.Label(master, text="GF(2^m); m=").grid(row=4, column=1, ipadx=200)
        tk.Label(master, text="", ).grid(row=5, column=1, ipadx=200)
        tk.Label(master, text="Results", bg="yellow").grid(row=6, column=1, ipadx=200)
        tk.Label(master, text="Decimal:").grid(row=7, column=1, ipadx=200)
        tk.Label(master, text="Binary:").grid(row=8, column=1, ipadx=200)
        tk.Label(master, text="Hexadecimal:").grid(row=9, column=1, ipadx=200)

        polBin1, polBin2, polHex1, polHex2, gf = tk.Entry(master), tk.Entry(master), tk.Entry(master), \
                                                 tk.Entry(master), tk.Entry(master)

        polBin1.grid(row=0, column=2)
        polBin2.grid(row=1, column=2)
        polHex1.grid(row=2, column=2)
        polHex2.grid(row=3, column=2)
        gf.grid(row=4, column=2)

        self.la = tk.Label(master, text="", fg="black", pady=10, padx=10, font=10)
        self.la.grid(row=10, column=2, ipadx=0)
        tk.Label(master, text="Irreducible Polynomial:", fg="black").grid(row=10, column=1,
                                                                          ipadx=0)

        addi = tk.Button(master, text="Add", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(0, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        addi.grid(row=0, column=0)

        subs = tk.Button(master, text="Sub", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(1, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        subs.grid(row=1, column=0)

        mult = tk.Button(master, text="Mul", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(2, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        mult.grid(row=2, column=0)

        divi = tk.Button(master, text="Div ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(3, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        divi.grid(row=3, column=0)

        invr = tk.Button(master, text="Inv ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(4, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        invr.grid(row=4, column=0)

        redu = tk.Button(master, text="Red", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(5, polBin1.get(), polBin2.get(), polHex1.get(), polHex2.get(),
                                                         gf.get()))
        redu.grid(row=5, column=0)

        self.FlabelD = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.FlabelD.grid(row=7, column=2)
        self.scrollerD = tk.Scrollbar(master, command=self.FlabelD.yview)
        self.scrollerD.grid(row=7, column=3, sticky='nsew')
        self.FlabelD['yscrollcommand'] = self.scrollerD.set
        copyDec = tk.Button(master, text="Copy Dec Value", padx=30, pady=5,
                         command=lambda: tools.addToClipBoard(self.FlabelD.get('1.0', END)))
        copyDec.grid(row=7, column=4)

        self.FlabelB = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.FlabelB.grid(row=8, column=2)
        self.scrollerB = tk.Scrollbar(master, command=self.FlabelB.yview)
        self.scrollerB.grid(row=8, column=3, sticky='nsew')
        self.FlabelB['yscrollcommand'] = self.scrollerB.set
        copyBin = tk.Button(master, text="Copy Bin Value", padx=30, pady=5,
                            command=lambda: tools.addToClipBoard(self.FlabelB.get('1.0', END)))
        copyBin.grid(row=8, column=4)

        self.FlabelH = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.FlabelH.grid(row=9, column=2)
        self.scrollerH = tk.Scrollbar(master, command=self.FlabelH.yview)
        self.scrollerH.grid(row=9, column=3, sticky='nsew')
        self.FlabelH['yscrollcommand'] = self.scrollerH.set
        copyHex = tk.Button(master, text="Copy Hex Value", padx=30, pady=5,
                            command=lambda: tools.addToClipBoard(self.FlabelH.get('1.0', END)))
        copyHex.grid(row=9, column=4)

        menubinAr = tk.Menu(master)
        filemenu = tk.Menu(menubinAr, tearoff=0)
        # filemenu.add_separator()
        # menubinAr.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubinAr, tearoff=0)
        helpmenu.add_command(label="More info", command=lambda: self.popupMessage("Polynomial Calculator", "More info"))
        helpmenu.add_command(label="About", command=lambda: self.popupMessage(
            "Developed by Peter Farah, Anthony Saab, and Karim Ghaddar for EECE455 Project#3", "About", "600x80"))
        menubinAr.add_cascade(label="Help", menu=helpmenu)

        master.config(menu=menubinAr)
        w, h = master.winfo_screenwidth(), master.winfo_screenheight()
        master.geometry("%dx%d+0+0" % (w, h))
        master.mainloop()

    def popupMessage(self, message, tit="Warning!", size="400x100"):
        """
        Display a custom error message for the user
        """
        popup = tk.Tk()
        popup.geometry(size)
        popup.wm_title(tit)
        label = tk.Label(popup, text=message, font="NORM_FONT")
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="OK", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def checkInput(self, mode, binA, binB, hexA, hexB, m):
        """
        Checks user input for unacceptable input forms
        :param mode: int representing the operation requested by user
        :param binA: str value of binary field #1
        :param binB: str value of binary field #2
        :param hexA: str value of hex field #1
        :param hexB: str value of hex field #2
        :param m: int for the m(2^m)
        """
        binA, binB, hexA, hexB, m = binA.strip(), binB.strip(), hexA.strip(), hexB.strip(), m.strip()
        if binA[:2] == "0b":
            binA = binA[2:]
        if binB[:2] == "0b":
            binB = binB[2:]
        if hexA[:2] == "0x":
            hexA = hexA[2:]
        if hexB[:2] == "0x":
            hexB = hexB[2:]
        lenBinA, lenBinB, lenHexA, lenHexB, lenM = len(binA), len(binB), len(hexA), len(hexB), len(m)
        filledFields = []
        if binA:
            filledFields.append([2, binA])
        if binB:
            filledFields.append([2, binB])
        if hexA:
            filledFields.append([16, hexA])
        if hexB:
            filledFields.append([16, hexB])
        if lenM == 0:
            self.popupMessage("Please specify 'm' for the 2^m Galois Field")
        elif mode <= 3 and len(filledFields) != 2:
            self.popupMessage("For this operation, provide only 2 polynomials")
        elif mode >= 4 and len(filledFields) != 1:
            self.popupMessage("For this operation, provide only 1 polynomial")
        elif not m.isnumeric():
            self.popupMessage("Galois only takes integer")
        elif lenBinA != 0 and not tools.isBin(binA):
            self.popupMessage("Bin1 invalid input")
        elif lenBinB != 0 and not tools.isBin(binB):
            self.popupMessage("Bin2 invalid input")
        elif lenHexA != 0 and not tools.isHex(hexA):
            self.popupMessage("Hex1 invalid input")
        elif lenHexB != 0 and not tools.isHex(hexB):
            self.popupMessage("Hex2 invalid input")
        elif not self.myConnector.checkIfSupported(int(m)):
            self.popupMessage("GF(2^" + str(m) + ") not supported")
        else:
            self.myConnector.calculate(mode, filledFields, int(m))

    def updateResult(self, resultInDec, irreducibleSt):
        """
        Called by the backend to show the results on the GUI
        :param resultInDec: Resulting polynomial in decimal representation
        :param irreducibleSt: str of the irreducible polynomial used for the successful oepration
        """
        stDec = str(resultInDec)
        self.FlabelD['state'] = 'normal'
        self.FlabelD.delete('1.0', END)
        self.FlabelD.insert("1.0", stDec)
        self.FlabelD['state'] = 'disabled'

        finalsb = str(bin(int(resultInDec)))
        finalsh = str(hex(int(resultInDec)))
        self.FlabelB['state'] = 'normal'
        self.FlabelB.delete('1.0', END)
        self.FlabelB.insert("1.0", finalsb)
        self.FlabelB['state'] = 'disabled'

        self.FlabelH['state'] = 'normal'
        self.FlabelH.delete('1.0', END)
        self.FlabelH.insert("1.0", finalsh)
        self.FlabelH['state'] = 'disabled'
        self.la['text'] = irreducibleSt
