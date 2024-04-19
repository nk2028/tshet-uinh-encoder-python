from pathlib import Path; import sys; sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

import TshetUinhEncoder as TE

def assert_equal(a, b):
    if a != b:
        raise ValueError(f'{a} and {b} are not equal!')

音韻地位1 = TE.音韻地位.from描述('幫三凡入')
assert_equal(音韻地位1.清濁, '全清')
assert_equal(音韻地位1.音, '脣')
assert_equal(音韻地位1.組, '幫')
assert_equal(音韻地位1.攝, '咸')
assert_equal(音韻地位1.類, '方')
assert_equal(音韻地位1.描述, '幫三凡入')
assert_equal(音韻地位1.最簡描述, '幫凡入')
assert_equal(音韻地位1.表達式, '幫母 三等 凡韻 入聲')
assert_equal(音韻地位1.最簡表達式, '幫母 凡韻 入聲')
assert_equal(音韻地位1.編碼, 'A9D')
assert_equal(音韻地位1.屬於('章母'), False)
assert_equal(音韻地位1.屬於('一四等'), False)
assert_equal(音韻地位1.屬於('幫組 或 陽韻'), True)

音韻地位2 = TE.音韻地位.from描述('羣開三A支平')
assert_equal(音韻地位2.清濁, '全濁')
assert_equal(音韻地位2.音, '牙')
assert_equal(音韻地位2.組, '見')
assert_equal(音韻地位2.攝, '止')
assert_equal(音韻地位2.類, '渠')
assert_equal(音韻地位2.描述, '羣開三A支平')
assert_equal(音韻地位2.最簡描述, '羣開A支平')
assert_equal(音韻地位2.表達式, '羣母 開口 三等 重紐A類 支韻 平聲')
assert_equal(音韻地位2.最簡表達式, '羣母 開口 重紐A類 支韻 平聲')
assert_equal(音韻地位2.編碼, 'fFA')

assert 音韻地位1 != 音韻地位2
assert 音韻地位1 > 音韻地位2

音韻地位3 = TE.音韻地位.from描述('幫三凡入')
assert 音韻地位1 == 音韻地位3
assert len({音韻地位1, 音韻地位3}) == 1

# 測試欣韻和眞韻的容錯
assert TE.音韻地位.from描述('影開三A眞平').描述 == '影開三A真平'
assert TE.音韻地位.from描述('溪開三欣上').描述 == '溪開三殷上'
