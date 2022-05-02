import re
import math
import unicodedata

largeNumbers = {'兆': 1000000000000, '億': 100000000, '万': 10000}
smallNumbers = {'千': 1000, '百': 100, '十': 10}
japaneseNumerics = {'〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                    '０': 0, '１': 1, '２': 2, '３': 3, '４': 4, '５': 5, '６': 6, '７': 7, '８': 8, '９': 9}
oldJapaneseNumerics = {'零': '〇', '壱': '一', '壹': '一', '弐': '二', '弍': '二', '貳': '二', '貮': '二', '参': '三',
                       '參': '三', '肆': '四', '伍': '五', '陸': '六', '漆': '七', '捌': '八', '玖': '九', '拾': '十', '廿': '二十',
                       '陌': '百', '佰': '百', '阡': '千', '仟': '千', '萬': '万'}


def normalize(japanese):
    for key in oldJapaneseNumerics:
        japanese = japanese.replace(key, oldJapaneseNumerics[key])
    return japanese


# 漢数字を兆、億、万単位に分割する
def splitLargeNumber(japanese):
    kanji = japanese
    numbers = {}
    for key in largeNumbers:
        match = re.findall(f'(.+){key}', kanji)
        if match:
            numbers[key] = kan2n(match[0])
            kanji = kanji.replace(match[0]+key, '')
        else:
            numbers[key] = 0
    if kanji:
        numbers['千'] = kan2n(kanji)
    else:
        numbers['千'] = 0
    return numbers


def kan2n(japanese):
    if re.findall('^[0-9]+$', japanese):
        return(int(japanese))

    kanji = zen2han(japanese)
    number = 0
    for key in smallNumbers:
        match = re.findall(f'(.*){key}', kanji)
        if match:
            n = 1
            if match[0]:
                if re.findall('^[0-9]+$', match[0]):
                    n = int(match[0])
                else:
                    n = japaneseNumerics[match[0]]
            number = number + (n * smallNumbers[key])
            kanji = kanji.replace(match[0]+key, '')
    if kanji:
        if re.findall('^[0-9]+$', kanji):
            number = number + int(kanji)
        else:
            number = number + japaneseNumerics[kanji]
    return number


def n2kan(num):
    kanjiNumbers = list(japaneseNumerics.keys())
    number = int(num)
    kanji = ''
    for key in smallNumbers:
        n = math.floor(number / smallNumbers[key])
        if n:
            number = number - (n * smallNumbers[key])
            if (1 == n):
                kanji = f'{kanji}{key}'
            else:
                kanji = f'{kanji}{kanjiNumbers[n]}{key}'
    if number:
        kanji = f'{kanji}{kanjiNumbers[number]}'
    return(kanji)


def zen2han(str):
    return unicodedata.normalize("NFKC", str)
