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
            if 呼 == '':
                呼 = None
            if 重紐 == '':
                重紐 = None
            roundtrip1(母, 呼, 等, 重紐, 韻, 聲)
            roundtrip2(母, 呼, 等, 重紐, 韻, 聲)


def test_韻目到韻():
    '''
    測試韻目到韻。
    '''
    assert QieyunEncoder.韻目到韻('物') == '文'
    assert QieyunEncoder.韻目到韻('敬') == '庚'
    assert QieyunEncoder.韻目到韻('東') == '東'


def test_母到清濁():
    '''
    測試母到清濁。
    '''
    assert QieyunEncoder.母到清濁('端') == '全清'
    assert QieyunEncoder.母到清濁('以') == '次濁'


def test_母到音():
    '''
    測試母到音。
    '''
    assert QieyunEncoder.母到音('並') == '脣'
    assert QieyunEncoder.母到音('羣') == '牙'


def test_韻到攝():
    '''
    測試韻到攝。
    '''
    assert QieyunEncoder.韻到攝('冬') == '通'
    assert QieyunEncoder.韻到攝('侵') == '深'


def test_欣韻和眞韻的容錯():
    '''
    測試欣韻和眞韻的容錯。
    '''
    assert QieyunEncoder.音韻地位.from描述('影開三A眞平').描述 == '影開三A真平'
    assert QieyunEncoder.音韻地位.from描述('溪開三欣上').描述 == '溪開三殷上'
