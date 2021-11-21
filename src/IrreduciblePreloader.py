import galois
import json
import sys
import os


class IrreduciblePreloader:
    """
    Instantiating this class loads the preloaded json file of irreducible polynomials.
    If the file does not exist, the class will generate it using the galois pypi package.
    """
    dict = {}
    ready = False

    def __init__(self):
        try:
            # Case everything is bundled in a standalone EXE file (really everything)
            if getattr(sys, 'frozen', False):
                nameHandle = open(os.path.join(sys._MEIPASS, "Preloaded_Irreducibles.json"), "r")
            else:
                nameHandle = open("../resources/Preloaded_Irreducibles.json", "r")
            tempDict = json.loads(nameHandle.read())
            for key in tempDict:
                self.dict[int(key)] = json.loads(tempDict[key])
        except FileNotFoundError:
            nameHandle = open("../resources/Preloaded_Irreducibles.json", "w")
            nameHandle.write("{")
            for m in range(2, 201):
                newEntry = galois.irreducible_poly(2, m).coeffs.tolist()
                self.dict[m] = newEntry
                nameHandle.write('"' + str(m) + '":"' + str(newEntry) + '",')
            nameHandle.write('"-1":"0"')
            nameHandle.write("}")
        finally:
            nameHandle.close()
        ready = True
