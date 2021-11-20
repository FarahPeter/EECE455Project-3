from numpy import poly1d

import tools
from IrreduciblePreloader import IrreduciblePreloader
from PolyGalois2m import PolyGalois2m


class FrontToBackConnector:
    myPreloader = None
    myGUI = None

    def __init__(self, connector):
        connector.append(self)
        self.myPreloader = IrreduciblePreloader()

    def checkIfSupported(self, m):
        if m in self.myPreloader.dict:
            return True, self.myPreloader.dict[m]
        else:
            return False

    def treatEntry(self, entry):
        entry[1] = list(entry[1])
        if entry[0] == 16:
            entry[1] = tools.hexToBin(entry[1])
        entry[1] = tools.charListToIntList(entry[1])
        return entry[1]

    def calculate(self, mode, filledFields, m):
        treatedEntries = []
        for i in range(len(filledFields)):
            treatedEntries.append(self.treatEntry(filledFields[i]))
        irreducibleCoeffs = self.myPreloader.dict[m]
        polynomials = [PolyGalois2m(coeffs, m, irreducibleCoeffs) for coeffs in treatedEntries]
        irreducibleSt = tools.stringifyBinList(irreducibleCoeffs)
        if mode == 0:
            result = polynomials[0] + polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        elif mode == 1:
            result = polynomials[0] - polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        elif mode == 2:
            result = polynomials[0] * polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        elif mode == 3:
            result = polynomials[0] / polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        elif mode == 4:
            result = polynomials[0].findInverse()
            self.myGUI.updateResult(tools.binListToDec(result.coeffs), irreducibleSt)
        elif mode == 5:
            result = polynomials[0]
            self.myGUI.updateResult(tools.binListToDec(result.coeffs), irreducibleSt)
