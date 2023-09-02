import random


def generateRandomCordinates( range1:list = [0,500], range2:list = [0,450] ):
    return (random.randint(range1[0],range1[1]),random.randint(range2[0],range2[1]))

