import numpy as np
import galois


class PolyGalois2m:
    numPoly = None
    m = None
    irreducible = None

    def __init__(self, coeffs, m, irreducibleCoeffs):
        """
        Automatically submit the coeffs to a mod 2 operation,
        then creates a np.poly1d from that modified coeffs and
        submits it to a mod m(x) operation, where m(x) is the irreducible
        polynomial given in the irreducibleCoeffs argument

        :param coeffs: List of int(0) and int(1)
        :param m: int indicating the power of 2 to be used for galois field
        :param irreducibleCoeffs: can be a list of int(0) and int(1), or a np.poly1d()
        """
        self.numPoly = np.poly1d(coeffs)
        self.numPoly = self.coeffsMod2(self.numPoly)
        if type(irreducibleCoeffs) == list:
            self.irreducible = np.poly1d(irreducibleCoeffs)
        else:
            self.irreducible = irreducibleCoeffs
        self.irreducible = self.coeffsMod2(self.irreducible)
        self.polyModIrreducible()
        self.m = m

    def findQuotients(self, dividend, divisor):
        quotients = []
        while True:
            (quotient, remainder) = dividend / divisor
            remainder = self.coeffsMod2(remainder)
            quotient = self.coeffsMod2(quotient)
            quotients.append(quotient)

            if len(remainder.coeffs) == 1:
                return quotients
            else:
                dividend = divisor
                divisor = remainder

    def findInverse(self):
        a2 = np.poly1d([0])
        b2 = np.poly1d([1])
        quotients = self.findQuotients(self.irreducible, self.numPoly)
        for i in range(len(quotients)):
            oldA2 = a2
            a2 = b2
            b2 = oldA2 - quotients[i] * a2
        b2 = self.coeffsMod2(b2)
        return b2

    def __add__(self, other):
        temp = PolyGalois2m(self.numPoly + other.numPoly, self.m, self.irreducible)
        temp.polyModIrreducible()
        return temp

    def __sub__(self, other):
        temp = PolyGalois2m(self.numPoly - other.numPoly, self.m, self.irreducible)
        temp.polyModIrreducible()
        return temp

    def __mul__(self, other):
        temp = PolyGalois2m(self.numPoly * other.numPoly, self.m, self.irreducible)
        temp.polyModIrreducible()
        return temp

    def __floordiv__(self, other):
        (quotient, remainder) = self.numPoly / other.numPoly
        temp = PolyGalois2m(quotient, self.m, self.irreducible)
        temp.polyModIrreducible()
        return temp

    def __str__(self):
        return str(self.numPoly)

    def __mod__(self, other):
        print(self, other)
        print("\n", self.irreducible)
        (quotient, remainder) = self.numPoly / other.numPoly
        temp = PolyGalois2m(remainder, self.m, self.irreducible)
        temp.polyModIrreducible()
        return temp

    def polyModIrreducible(self):
        (quotient, remainder) = self.numPoly / self.irreducible
        self.numPoly = remainder
        self.numPoly = self.coeffsMod2(self.numPoly)

    def coeffsMod2(self, toMod):
        newCoeffs = [0] * len(toMod.coeffs)
        for i in range(len(toMod.coeffs)):
            if toMod.coeffs[i] % 2:
                newCoeffs[i] = 1
        return np.poly1d(newCoeffs)
