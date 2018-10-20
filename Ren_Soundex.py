class soundexer:
    #length is the length of the soundex returned by the object
    def __init__(self, length=4):
        self.DICT = {"1":("b", "f", "p", "v"),
              "2":("c","g","j","k","q","s","x","z"),
              "3":("d", "t"),
              "4":("l"),
              "5":("m", "n"),
              "6":("r")}
        self.length = length

    #builds a list and appends values according to the soundex algorithm
    #   and then joins that list at the end
    def soundex(self, string):
        counter = 0
        if string != "":
            tempSoundex = [string[0]]
            for x in string:
                counter += 1
                if counter == 1:
                    continue
                if counter <= self.length:
                    tempSoundex.append(self.getNumber(x))
        returnSoundex = "".join(tempSoundex)
        return returnSoundex

    #used in creating the soundex; returns the number from the dictionary
    def getNumber(self, string):
        return self.DICT(string)
        
