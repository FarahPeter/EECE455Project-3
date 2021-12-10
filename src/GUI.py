import tkinter as tk
import tools
from tkinter import END


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
        master.geometry("1300x600")

        # Labels for fields/textboxes
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
        tk.Label(master, text="Irreducible Polynomial:", fg="black").grid(row=10, column=1,
                                                                          ipadx=0)

        # Input fields
        self.polBin1, self.polBin2, self.polHex1, self.polHex2, self.gf = tk.Entry(master), tk.Entry(master), tk.Entry(master), \
                                                 tk.Entry(master), tk.Entry(master)
        self.polBin1.grid(row=0, column=2), self.polBin2.grid(row=1, column=2), self.polHex1.grid(row=2, column=2)
        self.polHex2.grid(row=3, column=2), self.gf.grid(row=4, column=2)
        self.polBin1.config(width=70), self.polBin2.config(width=70), self.polHex1.config(width=70)
        self.polHex2.config(width=70), self.gf.config(width=70)

        # Buttons for submitting
        addi = tk.Button(master, text="     Add    ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(0, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        addi.grid(row=0, column=0)
        subs = tk.Button(master, text="  Subtract  ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(1, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        subs.grid(row=1, column=0)
        mult = tk.Button(master, text="  Multiply  ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(2, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        mult.grid(row=2, column=0)
        divi = tk.Button(master, text="   Divide   ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(3, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        divi.grid(row=3, column=0)
        invr = tk.Button(master, text="Find Inverse", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(4, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        invr.grid(row=4, column=0)
        redu = tk.Button(master, text="    Reduce   ", padx=30, pady=5, fg="black", bg="#263D42",
                         command=lambda: self.checkInput(5, self.polBin1.get(), self.polBin2.get(), self.polHex1.get(), self.polHex2.get(),
                                                         self.gf.get()))
        redu.grid(row=5, column=0)

        clearAll = tk.Button(master, text="Clear All Inputs", padx=30, pady=5,
                            command=lambda: self.clearAllInputs())
        clearAll.grid(row=2, column=4)

        # Dec Output field
        self.outputDecText = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.outputDecText.grid(row=7, column=2)
        self.scrollerD = tk.Scrollbar(master, command=self.outputDecText.yview)
        self.scrollerD.grid(row=7, column=3, sticky='nsew')
        self.outputDecText['yscrollcommand'] = self.scrollerD.set
        copyDec = tk.Button(master, text="Copy Dec Value", padx=30, pady=5,
                            command=lambda: tools.addToClipBoard(master, self.outputDecText.get('1.0', END)))
        copyDec.grid(row=7, column=4)

        # Bin Output field
        self.outputBinText = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.outputBinText.grid(row=8, column=2)
        self.scrollerB = tk.Scrollbar(master, command=self.outputBinText.yview)
        self.scrollerB.grid(row=8, column=3, sticky='nsew')
        self.outputBinText['yscrollcommand'] = self.scrollerB.set
        copyBin = tk.Button(master, text="Copy Bin Value", padx=30, pady=5,
                            command=lambda: tools.addToClipBoard(master, self.outputBinText.get('1.0', END)))
        copyBin.grid(row=8, column=4)

        # Hex Output field
        self.outputHexText = tk.Text(master, state='disabled', bg='grey', fg="white", height=5, width=52)
        self.outputHexText.grid(row=9, column=2)
        self.scrollerH = tk.Scrollbar(master, command=self.outputHexText.yview)
        self.scrollerH.grid(row=9, column=3, sticky='nsew')
        self.outputHexText['yscrollcommand'] = self.scrollerH.set
        copyHex = tk.Button(master, text="Copy Hex Value", padx=30, pady=5,
                            command=lambda: tools.addToClipBoard(master, self.outputHexText.get('1.0', END)))
        copyHex.grid(row=9, column=4)

        # Irreducible Output field
        self.outputIrreducible = tk.Label(master, text="", fg="black", pady=10, padx=10, font=10)
        self.outputIrreducible.grid(row=10, column=2, ipadx=0)

        # Master window setup
        menubinAr = tk.Menu(master)
        helpmenu = tk.Menu(menubinAr, tearoff=0)
        helpmenu.add_command(label="More info", command=lambda: self.popupMessage("Polynomial Calculator", "More info"))
        helpmenu.add_command(label="About", command=lambda: self.popupMessage(
            "Developed by Peter Farah, Anthony Saab, and Karim Ghaddar for EECE455 Project#3", "About", "1000x100"))
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
        elif mode == 3 and not int(filledFields[1][1]):
            self.popupMessage("Cannot divide by 0")
        elif mode == 4 and tools.allZeroes(filledFields[0][1]):
            self.popupMessage("Cannot invert by 0")
        else:
            self.myConnector.calculate(mode, filledFields, int(m))

    def updateResult(self, resultInDec, irreducibleSt):
        """
        Called by the backend to show the results on the GUI
        :param resultInDec: Resulting polynomial in decimal representation
        :param irreducibleSt: str of the irreducible polynomial used for the successful oepration
        """
        stDec = str(resultInDec)
        self.outputDecText['state'] = 'normal'
        self.outputDecText.delete('1.0', END)
        self.outputDecText.insert("1.0", stDec)
        self.outputDecText['state'] = 'disabled'

        finalsb = str(bin(int(resultInDec)))
        finalsh = str(hex(int(resultInDec)))
        self.outputBinText['state'] = 'normal'
        self.outputBinText.delete('1.0', END)
        self.outputBinText.insert("1.0", finalsb)
        self.outputBinText['state'] = 'disabled'

        self.outputHexText['state'] = 'normal'
        self.outputHexText.delete('1.0', END)
        self.outputHexText.insert("1.0", finalsh)
        self.outputHexText['state'] = 'disabled'
        self.outputIrreducible['text'] = irreducibleSt

    def clearAllInputs(self):
        """
        Clears all input fields
        :return:
        """
        self.polBin1.delete(0, END)
        self.polBin2.delete(0, END)
        self.polHex1.delete(0, END)
        self.polHex2.delete(0, END)
        self.gf.delete(0, END)
