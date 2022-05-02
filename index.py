import re
import math
from utils import normalize, splitLargeNumber, largeNumbers, n2kan, japaneseNumerics


def kanji2number(japanese: str):
    japanese = normalize(japanese)

    if (re.findall('〇', japanese) or re.findall('^[〇一二三四五六七八九]+$', japanese)):
        for key in japaneseNumerics:
            japanese = japanese.replace(key, str(japaneseNumerics[key]))
        return int(japanese)

    else:
        number = 0
        numbers = splitLargeNumber(japanese)

        # 万位上の数字を数値に変換
        for key in largeNumbers:
            if numbers[key]:
                n = largeNumbers[key] * numbers[key]
                number = number + n

        if (type(number) != int or type(numbers['千']) != int):
            print("The attribute of kanji2number() must be a Japanese numeral as integer.")

        return number + numbers['千']


def number2kanji(num: int):
    if re.findall('^[0-9]+$', str(num)) == []:
        print('The attribute of number2kanji() must be integer.')
        return
    number = int(num)
    kanji = ''
    for key in largeNumbers:
        n = math.floor(number / largeNumbers[key])
        if n:
            number = number - (n * largeNumbers[key])
            kanji = f'{kanji}{n2kan(n)}{key}'

    if number:
        kanji = f'{kanji}{n2kan(number)}'

    return kanji

# '５兆え八萬90千拾壹あ'
# > Array ["５兆", "", "八萬90千拾壹", "", ""]


def findKanjiNumbers(text: str):
    num = '[0-9０-９]+|[〇一二三四五六七八九壱壹弐弍貳貮参參肆伍陸漆捌玖]+'
    basePattern = f'({num})?(千|阡|仟)|({num})?(百|陌|佰)|({num})?(十|拾)|({num})?'
    pattern = f'{basePattern}(兆)|{basePattern}(億)|{basePattern}(万|萬)|{basePattern}'
    match = re.findall(pattern, text)

    if match:
        match_list = [''.join(tups) for tups in match]
        match_list = ' '.join(match_list)
        match_list = match_list.split('  ')
        match_list = [i.replace(' ', '') for i in match_list]
        # print(match_list)
        #print([item for item in match_list])
        result = [item for item in match_list if (re.findall(
            '^[0-9０-９]+$', item) == [] and len(item) != 0 and item not in ['兆', '億', '万', '萬'])]
        return result
    else:
        return


def kanji2int(string: str):
    kanjiNumbers = findKanjiNumbers(string)
    for i in range(len(kanjiNumbers)):
        string = string.replace(kanjiNumbers[i], str(kanji2number(kanjiNumbers[i])))
    return string
