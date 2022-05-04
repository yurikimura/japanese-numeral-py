from index import *
from utils import *


def test_n2kan():
    assert n2kan(1111) == '千百十一'
    assert n2kan(3111) == '三千百十一'
    assert n2kan(1000) == '千'
    assert n2kan(5) == '五'


def test_kan2n():
    assert kan2n('三千') == 3000
    assert kan2n('22') == 22
    assert kan2n('１２３') == 123


def test_kanji2number():
    assert kanji2number('一千百十一兆一千百十一億一千百十一万一千百十一') == 1111111111111111
    assert kanji2number('一千百十一兆一千百十一億一千百十一万') == 1111111111110000
    assert kanji2number('一千百十一兆一千百十一億一千百十一') == 1111111100001111
    assert kanji2number('百十一') == 111
    assert kanji2number('三億八') == 300000008
    assert kanji2number('三百八') == 308
    assert kanji2number('三〇八') == 308
    assert kanji2number('二〇二〇') == 2020
    assert kanji2number('二千') == 2000
    assert kanji2number('壱万') == 10000
    assert kanji2number('弍万') == 20000
    assert kanji2number('一二三四') == 1234
    assert kanji2number('壱阡陌拾壱兆壱阡陌拾壱億壱阡陌拾壱萬壱阡陌拾壱') == 1111111111111111
    assert kanji2number('壱仟佰拾壱兆壱仟佰拾壱億壱仟佰拾壱萬壱仟佰拾壱') == 1111111111111111


def test_number2kanji():
    assert number2kanji(1111111111111111) == '千百十一兆千百十一億千百十一万千百十一'
    assert number2kanji(1111113111111111) == '千百十一兆千百三十一億千百十一万千百十一'
    assert number2kanji(1000000000000000) == '千兆'
    assert number2kanji(1200000) == '百二十万'
    assert number2kanji(18) == '十八'
    assert number2kanji(100100000) == '一億十万'


def test_findKanjiNumbers():
    assert findKanjiNumbers('今日は二千二十年十一月二十日です。') == ['二千二十', '十一', '二十']
    assert findKanjiNumbers('今日は二〇二〇年十一月二十日です。') == ['二〇二〇', '十一', '二十']
    assert findKanjiNumbers('わたしは二千二十億円もっています。') == ['二千二十億']
    assert findKanjiNumbers('わたしは二〇二〇億円もっています。') == ['二〇二〇億']
    assert findKanjiNumbers('今日のランチは八百六十三円でした。') == ['八百六十三']
    assert findKanjiNumbers('今日のランチは八六三円でした。') == ['八六三']
    assert findKanjiNumbers('今月のお小遣いは三千円です。') == ['三千']
    assert findKanjiNumbers('青森県五所川原市金木町喜良市千苅６２−８') == ['五', '千']
    assert findKanjiNumbers('わたしは1億2000万円もっています。') == ['1億2000万']
    # assert findKanjiNumbers('香川県仲多度郡まんのう町勝浦字家六２０９４番地１') == ['六']


def test_findKanjiNumbers_errors():
    assert findKanjiNumbers('栗沢町万字寿町') == []
    assert findKanjiNumbers('私は億ションに住んでいます') == []


def test_findKanjiNumbers_random():
    assert findKanjiNumbers('今日は２千20年十一月二十日です。') == ['２千20', '十一', '二十']


def test_findKanjiNumbers_old():
    assert findKanjiNumbers('私が住んでいるのは壱番館の弐号室です。') == ['壱', '弐']
    assert findKanjiNumbers('私は、ハイツ弍号棟に住んでいます。') == ['弍']
    assert findKanjiNumbers('私は、壱阡陌拾壱兆壱億壱萬円持っています。') == ['壱阡陌拾壱兆壱億壱萬']
    assert findKanjiNumbers('私は、壱仟佰拾壱兆壱億壱萬円持っています。') == ['壱仟佰拾壱兆壱億壱萬']


def test_kanji2number():
    assert kanji2number('100万') == 1000000
    assert kanji2number('5百') == 500
    assert kanji2number('7十') == 70
    assert kanji2number('4千８百') == 4800
    assert kanji2number('4千８百万') == 48000000
    assert kanji2number('3億4千８百万') == 348000000
    assert kanji2number('3億4千８百万6') == 348000006
    assert kanji2number('2百億') == 20000000000


def test_kanji2number_random():
    assert kanji2number('4千8百21') == 4821
    assert kanji2number('1千2百35億8百21') == 123500000821
    assert kanji2number('2億3千430万') == 234300000
    assert kanji2number('２億３千４５６万７８９０') == 234567890
    assert kanji2number('１２３') == 123


def test_issues():
    #assert findKanjiNumbers('香川県仲多度郡まんのう町勝浦字家六２０９４番地１') == ['六']
    assert findKanjiNumbers('今日は２千20年十一月二十日です。') == ['２千20', '十一', '二十']


def test_kanji2int():
    assert kanji2int('今日は二千二十年十一月二十日です。') == '今日は2020年11月20日です。'
    assert kanji2int('今日は二〇二〇年十一月二十日です。') == '今日は2020年11月20日です。'
    assert kanji2int('わたしは二千二十億円もっています。') == 'わたしは202000000000円もっています。'
    #assert kanji2int('わたしは二〇二〇億円もっています。') == 'わたしは202000000000円もっています。'
    assert kanji2int('今日のランチは八百六十三円でした。') == '今日のランチは863円でした。'
    assert kanji2int('今日のランチは八六三円でした。') == '今日のランチは863円でした。'
    assert kanji2int('今月のお小遣いは三千円です。') == '今月のお小遣いは3000円です。'
    assert kanji2int('青森県五所川原市金木町喜良市千苅６２−８') == '青森県5所川原市金木町喜良市1000苅６２−８'
    assert kanji2int('わたしは1億2000万円もっています。') == 'わたしは120000000円もっています。'
