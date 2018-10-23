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
        counter = self.length
        returnSoundex = ""
        if string == "":
            return ""
        tempSoundex = []
        for x in string:
            if x.isalpha():
                if counter == self.length:
                    tempSoundex.append(x.upper())
                    counter -= 1
                    prevAppend = x.lower()
                    #else if x in dict, multiple consecutive letters w/ same number, and letters w same number not separated with h or w
                elif x in self.DICT and self.getNum(x.lower()) != self.getNum(prev) and ((self.getNum(x.lower()) != tempSoundex[len(tempSoundex)-1]) and (prev != "h" and prev !="w")):
                    if counter > 0:
                        #if not ((self.getNum(x.lower()) == tempSoundex[len(tempSoundex)-1]) or self.getNum(x.lower()) == self.getNum(prev)) and prevCounter == counter:
                        tempSoundex.append(self.getNum(x.lower()))
                        counter -= 1
                prev = x.lower()
            if counter == 0:
                break
        if len(tempSoundex) > 0:
            while counter >= 0:
                tempSoundex.append("0")
                counter -= 1
        returnSoundex = "".join(tempSoundex)
        return returnSoundex

    #used in creating the soundex; returns the number from the dictionary
    def getNum(self, string):
        return self.DICT[string]
        
