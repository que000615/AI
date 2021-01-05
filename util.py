import pinyin
import os

class Util:
    @staticmethod
    def toPinyin(string):
        return pinyin.get(string, format="strip", delimiter=" ")


if __name__ == "__main__":
    with open('word.txt','rb') as lines:
        for line in lines:
            word = line.split("=")[0]
            print(Util.toPinyin(word))