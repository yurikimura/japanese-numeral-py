こちらのライブラリのpythonバージョン（非公式）です。
https://github.com/geolonia/japanese-numeral 

Converts Japanese Kanji numeral <=> number.

## Installation

comming soon...

```bash
```

## Usage

### kanji2number()

Converts Japanese Kanji numeral to number.

```python
from JapaneseNumeric import kanji2number

kanji2number('一千百十一兆一千百十一億一千百十一万一千百十一') # 1111111111111111

# '一千' を '千' と記述しても同じ結果になる。
kanji2number('千百十一兆千百十一億千百十一万千百十一') # 1111111111111111

# 漢数字のゼロ '〇' を使用することも可能。
kanji2number('二〇二〇') # 2020

# 数字と漢数字が混ざった表記にも対応
kanji2number('2億3千430万') # 234300000
kanji2number('２億３千４５６万７８９０') # 234567890 （数字は全角でも可）
```

### number2kanji()

Converts number to Japanese Kanji numeral.

```python
from JapaneseNumeric import number2kanji

number2kanji(1111111111111111) # 千百十一兆千百十一億千百十一万千百十一
```

### findKanjiNumbers()

Finds the Japanese numeral numbers as an array.

```python
from JapaneseNumeric import findKanjiNumbers

findKanjiNumbers('今日は二千二十年十一月二十日です。') # [ '二千二十', '十一', '二十' ]
findKanjiNumbers('わたしは二千二十億円もっています。') # [ '二千二十億' ]
findKanjiNumbers('わたしは1億2000万円もっています。') # [ '1億2000万' ]
```

```python
from JapaneseNumeric import kanji2int

findKanjiNumbers('今日は二千二十年十一月二十日です。') # '今日は2020年11月20日です。'
```

## License

[MIT](LICENSE)
