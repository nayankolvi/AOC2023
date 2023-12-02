from common import rd
import os
import re
from collections import defaultdict

class CubeGame:
    def __init__(self, day, name):
        self.inputPath = os.path.join(os.getcwd(), day, name)
        self.data = rd.readLines(self.inputPath)
        self.dictGame = defaultdict(list)
        self.colorsDefault = {"red":12, "green":13, "blue":14}
        self.isExeeding = defaultdict(list)

    def validate(self):
        self.parser()
        allids = [int(id) for id in self.dictGame.keys() if self.isExeeding.get(id) == None]
        sumVal = sum(allids)
        print(f"Sum of part 1 is {sumVal}")

        # part 2
        powers = []
        for vals in self.dictGame.values():
            red, blue, green = [], [], []
            for item in vals:
                red.append(item["red"])
                green.append(item["green"])
                blue.append(item["blue"])
            powers.append(max(red)*max(green)*max(blue))

        sumVal = sum(powers)
        print(f"Sum part2 is {sumVal}")

    def parser(self):
        for line in self.data:
            #get game id
            splitData = line.split(":")
            id = ''.join(re.findall(r'\d+',splitData[0])).strip()
            allTurns = splitData[1].split(";")
            for val in allTurns:
                balls = val.split(",")
                colors = {"red":0, "blue":0, "green":0}
                for val in balls:
                    num = val.strip().split(" ")
                    colors[num[1].strip()] = int(num[0].strip())
                    if int(num[0].strip()) > int(self.colorsDefault[num[1].strip()]):
                        self.isExeeding[id].append(1) 
                
                self.dictGame[id].append(colors)

    def run(self):
        self.validate()
        pass

cg  = CubeGame("day2", "d2.txt")