from common import rd
import os
import re

class Calib:
    def __init__(self, day, name):
        self.inputPath = os.path.join(os.getcwd(), day, name)
        self.data = rd.readLines(self.inputPath)
        self.dictValNew = {"one": "o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"n9e"}
        # self.dictVal = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        pass

    def calibrate(self, part):
        self.values = []
        # find only digest in the sentence
        for sent in self.data:
            if part == "1":
                val = list(''.join(self.getDigits1(sent)))
            else:
                val = list(''.join(self.getDigits2(sent)))
            self.values.append(int(val[0]+val[-1]))
            

        result = sum(self.values)
        print(f"day1 part {part} result is :  {result}")

    def getDigits1(self, sentence):
        return re.findall(r'\d+', sentence)
    
    def getDigits2(self, sentence):
        # dataf = self.iterator(sentence, "forw")
        # datar = self.iterator(dataf, "back")
        for key in self.dictValNew.keys():
            sentence = sentence.replace(key, str(self.dictValNew[key]))

        return self.getDigits1(sentence)
    
    # logic to be checked, adding an extra 8 from somehwere
    # def iterator(self, sentence, type):
    #     keys = list(self.dictVal.keys())
    #     data = None
    #     word = ""
    #     if type == "back":
    #         sentence = ''.join(reversed(sentence))
    #     for letter in sentence:
    #         if type == "back":
    #             word = letter + word
    #         else:
    #             word = word + letter
    #         for key in keys:
    #             if key in word:
    #                 if type == "back":
    #                     sentence = ''.join(reversed(sentence))
    #                 data = sentence.replace(key, str(self.dictVal[key]))
    #                 if data == None:
    #                     return sentence
    #                 else:
    #                     return data
    #     if type == "back":
    #         return ''.join(reversed(sentence))
    #     else:     
    #         return sentence

    def run(self):
        self.calibrate("1")
        self.calibrate("2")



cal  = Calib("day1", "d1.txt")