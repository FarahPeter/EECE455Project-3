import tools
from IrreduciblePreloader import IrreduciblePreloader
from PolyGalois2m import PolyGalois2m


class FrontToBackConnector:
    myPreloader = None
    myGUI = None

    def __init__(self, connector):
        """
        Instantiates preloader and sends the self to the Launcher, so a link can be established.
        :param connector: Empty list used to return the self
        """
        connector.append(self)
        self.myPreloader = IrreduciblePreloader()

    def checkIfSupported(self, m):
        """
        Checks if the m provided corresponds to a supported GF(2^m)
        :param m: int
        :return: bool accordingly
        """
        if m in self.myPreloader.dict:
            return True, self.myPreloader.dict[m]
        else:
            return False

    def treatEntry(self, entry):
        """
        Takes an input from user in string form, could be bin or hex,
        converts it to binary list
        :param entry:
        :return: List of 0 and 1 coefficients, representing the equivalent polynomial inputted
        """
        if entry[0] == 16:
            entry[1] = tools.hexToBin(entry[1])
        else:
            entry[1] = list(entry[1])
        entry[1] = tools.charListToIntList(entry[1])
        return entry[1]

    def calculate(self, mode, filledFields, m):
        """
        Relays user input to backend in a suitable format
        :param mode: int representing the operation requested by user
        :param filledFields: list of tuples, each of which describes an input field value and base
        :param m: int for the m(2^m)
        """
        treatedEntries = []
        for i in range(len(filledFields)):
            treatedEntries.append(self.treatEntry(filledFields[i]))
        irreducibleCoeffs = self.myPreloader.dict[m]
        polynomials = [PolyGalois2m(coeffs, m, irreducibleCoeffs) for coeffs in treatedEntries]
        irreducibleSt = tools.stringifyBinList(irreducibleCoeffs)

        # Adding two polynomials
        if mode == 0:
            result = polynomials[0] + polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        # Substracting two polynomials
        elif mode == 1:
            result = polynomials[0] - polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        # Multiplying two polynomials
        elif mode == 2:
            result = polynomials[0] * polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        # Dividing two polynomials
        elif mode == 3:
            result = polynomials[0] / polynomials[1]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        # Inverting a polynomial
        elif mode == 4:
            result = polynomials[0].findInverse()
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
        # Moduloing a polynomial
        elif mode == 5:
            result = polynomials[0]
            self.myGUI.updateResult(tools.binListToDec(result.numPoly.coeffs), irreducibleSt)
