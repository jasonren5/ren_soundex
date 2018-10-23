class soundexer:
    #length is the length of the soundex returned by the object
    def __init__(self, length=4):
        self.DICT = {}
        self.DICT.update(dict.fromkeys(["a", "e", "i", "o", "u", "y", "h", "w"], ""))
        self.DICT.update(dict.fromkeys(["b", "f", "p", "v"], "1"))
        self.DICT.update(dict.fromkeys(["c","g","j","k","q","s","x","z"], "2"))
        self.DICT.update(dict.fromkeys(["d", "t"], "3"))
        self.DICT.update(dict.fromkeys(["l"], "4"))
        self.DICT.update(dict.fromkeys(["m", "n"], "5"))
        self.DICT.update(dict.fromkeys(["r"], "6"))
        self.length = length

    #builds a list and appends values according to the soundex algorithm
    #   and then joins that list at the end
    def soundex(self, string):
        counter = 0
        returnSoundex = ""
        if string == "":
            return ""
        tempSoundex = [string[0]]
        for x in string:
            if x in self.DICT:
                counter += 1
                if counter == 1:
                    continue
                if counter <= self.length:
                    tempSoundex.append(self.getNumber(x.lower()))
                    if (self.getNumber(x) == ""):
                        counter += -1
            else:
                continue
        for x in range(self.length-counter):
            tempSoundex.append("0")
        returnSoundex = "".join(tempSoundex)
        return returnSoundex

    #used in creating the soundex; returns the number from the dictionary
    def getNumber(self, string):
        return self.DICT[string]
        
