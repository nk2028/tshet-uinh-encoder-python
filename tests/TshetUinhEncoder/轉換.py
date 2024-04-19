from pathlib import Path; import sys; sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

import TshetUinhEncoder as TE

def assert_equal(a, b):
    if a != b:
        raise ValueError(f'{a} and {b} are not equal!')

assert_equal(TE.母到清濁('端'), '全清')
assert_equal(TE.母到清濁('以'), '次濁')
assert_equal(TE.母到組('滂'), '幫')
assert_equal(TE.母到組('云'), '影')
assert_equal(TE.母到組('以'), None)
assert_equal(TE.母到音('並'), '脣')
assert_equal(TE.母到音('羣'), '牙')
assert_equal(TE.母與等到類('見', '二'), '古')
assert_equal(TE.母與等到類('並', '三'), '符')
assert_equal(TE.韻到攝('冬'), '通')
assert_equal(TE.韻到攝('侵'), '深')
assert_equal(TE.韻目到韻('物'), '文')
assert_equal(TE.韻目到韻('敬'), '庚')
assert_equal(TE.韻目到韻('東'), '東')
