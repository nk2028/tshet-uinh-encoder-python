from os import path
import QieyunEncoder

here = path.abspath(path.dirname(__file__))


def roundtrip1(母, 呼, 等, 重紐, 韻, 聲):
    '''
    將音韻地位六要素轉換爲音韻編碼，再將音韻編碼轉換爲音韻地位六要素。

    用於測試轉換是否出現異常，以及轉換結果與轉換前是否一致。
    '''
    音韻地位 = QieyunEncoder.音韻地位(母, 呼, 等, 重紐, 韻, 聲)
    assert QieyunEncoder.音韻地位.from編碼(音韻地位.編碼) == 音韻地位


def roundtrip2(母, 呼, 等, 重紐, 韻, 聲):
    '''
    將音韻地位六要素轉換爲音韻描述，再將音韻描述轉換爲音韻地位六要素。

    用於測試轉換是否出現異常，以及轉換結果與轉換前是否一致。
    '''
    音韻地位 = QieyunEncoder.音韻地位(母, 呼, 等, 重紐, 韻, 聲)
    assert QieyunEncoder.音韻地位.from描述(音韻地位.描述) == 音韻地位


def test1():
    '''
    測試音韻編碼。
    '''
    with open(path.join(here, 'examples.txt'), encoding='utf8') as f:
        next(f)  # skip header
        for line in f:
            母, 呼, 等, 重紐, 韻, 聲 = line.rstrip('\n').split(',')
            if not 呼:
                呼 = None
            if not 重紐:
                重紐 = None
            roundtrip1(母, 呼, 等, 重紐, 韻, 聲)
            roundtrip2(母, 呼, 等, 重紐, 韻, 聲)


def test2():
    '''
    測試「法」字對應的音韻地位的各項音韻屬性。
    '''
    當前音韻地位 = QieyunEncoder.音韻地位.from描述('幫三凡入')

    assert 當前音韻地位.母 == '幫'
    assert 當前音韻地位.呼 == None
    assert 當前音韻地位.等 == '三'
    assert 當前音韻地位.重紐 == None
    assert 當前音韻地位.韻 == '凡'
    assert 當前音韻地位.聲 == '入'

    assert 當前音韻地位.清濁 == '全清'
    assert 當前音韻地位.音 == '脣'
    assert 當前音韻地位.攝 == '咸'

    assert 當前音韻地位.描述 == '幫三凡入'
    assert 當前音韻地位.最簡描述 == '幫凡入'
    assert 當前音韻地位.表達式 == '幫母 三等 凡韻 入聲'
    assert 當前音韻地位.編碼 == 'A9D'

    assert 當前音韻地位 == QieyunEncoder.音韻地位.from描述('幫凡入')


def test3():
    '''
    測試「祇」字對應的音韻地位的各項音韻屬性。
    '''
    當前音韻地位 = QieyunEncoder.音韻地位.from描述('羣開三A支平')

    assert 當前音韻地位.母 == '羣'
    assert 當前音韻地位.呼 == '開'
    assert 當前音韻地位.等 == '三'
    assert 當前音韻地位.重紐 == 'A'
    assert 當前音韻地位.韻 == '支'
    assert 當前音韻地位.聲 == '平'

    assert 當前音韻地位.清濁 == '全濁'
    assert 當前音韻地位.音 == '牙'
    assert 當前音韻地位.攝 == '止'

    assert 當前音韻地位.描述 == '羣開三A支平'
    assert 當前音韻地位.最簡描述 == '羣開A支平'
    assert 當前音韻地位.表達式 == '羣母 開口 三等 重紐A類 支韻 平聲'
    assert 當前音韻地位.編碼 == 'fFA'

    assert 當前音韻地位 == QieyunEncoder.音韻地位.from描述('羣開A支平')


def test4():
    '''
    測試「法」字對應的音韻地位的屬於函式
    '''
    當前音韻地位 = QieyunEncoder.音韻地位.from描述('幫三凡入')

    assert 當前音韻地位.屬於('幫母')
    assert 當前音韻地位.屬於('幫精組')
    assert not 當前音韻地位.屬於('精組')
    assert not 當前音韻地位.屬於('重紐A類 或 重紐B類')
    assert not 當前音韻地位.屬於('喉音')
    assert 當前音韻地位.屬於('仄聲')
    assert not 當前音韻地位.屬於('舒聲')
    assert 當前音韻地位.屬於('清音')
    assert not 當前音韻地位.屬於('全濁')
    assert not 當前音韻地位.屬於('次濁')
    assert 當前音韻地位.屬於('開合中立')
    assert not 當前音韻地位.屬於('開口 或 合口')
    assert 當前音韻地位.屬於('幫組 輕脣韻')
    assert not 當前音韻地位.屬於('陰聲韻')
    assert 當前音韻地位.判斷([
        ('遇果假攝 或 支脂之佳韻', ''),
        ('蟹攝 或 微韻', 'i'),
        ('效流攝', 'u'),
        ('深咸攝', [
            ('舒聲', 'm'),
            ('入聲', 'p')
        ]),
        ('臻山攝', [
            ('舒聲', 'n'),
            ('入聲', 't')
        ]),
        ('通江宕梗曾攝', [
            ('舒聲', 'ng'),
            ('入聲', 'k')
        ])
    ], '無韻尾規則') == 'p'


def test5():
    '''
    測試正則化韻。
    '''
    assert QieyunEncoder.正則化韻('物') == '文'
    assert QieyunEncoder.正則化韻('敬') == '庚'
    assert QieyunEncoder.正則化韻('東') == '東'
