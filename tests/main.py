from os import path
import TshetUinhEncoder as TE

here = path.abspath(path.dirname(__file__))

def roundtrip1(母, 呼, 等, 重紐, 韻, 聲):
    '''
    將音韻地位六要素轉換爲音韻編碼，再將音韻編碼轉換爲音韻地位六要素。

    用於測試轉換是否出現異常，以及轉換結果與轉換前是否一致。
    '''
    音韻地位 = TE.音韻地位(母, 呼, 等, 重紐, 韻, 聲)
    assert TE.音韻地位.from編碼(音韻地位.編碼) == 音韻地位

def roundtrip2(母, 呼, 等, 重紐, 韻, 聲):
    '''
    將音韻地位六要素轉換爲音韻描述，再將音韻描述轉換爲音韻地位六要素。

    用於測試轉換是否出現異常，以及轉換結果與轉換前是否一致。
    '''
    音韻地位 = TE.音韻地位(母, 呼, 等, 重紐, 韻, 聲)
    assert TE.音韻地位.from描述(音韻地位.描述) == 音韻地位

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
