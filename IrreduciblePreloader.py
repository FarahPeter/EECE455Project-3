import galois
import json


class IrreduciblePreloader:
    dict = {}
    ready = False

    def __init__(self):
        try:
            nameHandle = open("Preloaded_Irreducibles.json", "r")
            tempDict = json.loads(nameHandle.read())
            for key in tempDict:
                self.dict[int(key)] = json.loads(tempDict[key])
        except FileNotFoundError:
            nameHandle = open("Preloaded_Irreducibles.json", "w")
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