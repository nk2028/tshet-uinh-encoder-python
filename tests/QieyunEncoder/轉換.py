from pathlib import Path; import sys; sys.path.append(str(Path(__file__).resolve().parent.parent.parent / 'src'))

import QieyunEncoder as QE

def assert_equal(a, b):
    if a != b:
        raise ValueError(f'{a} and {b} are not equal!')

assert_equal(QE.母到清濁('端'), '全清')
assert_equal(QE.母到清濁('以'), '次濁')
assert_equal(QE.母到組('滂'), '幫')
assert_equal(QE.母到組('云'), '影')
assert_equal(QE.母到組('以'), None)
assert_equal(QE.母到音('並'), '脣')
assert_equal(QE.母到音('羣'), '牙')
assert_equal(QE.母與等到類('見', '二'), '古')
assert_equal(QE.母與等到類('並', '三'), '符')
assert_equal(QE.韻到攝('冬'), '通')
assert_equal(QE.韻到攝('侵'), '深')
assert_equal(QE.韻目到韻('物'), '文')
assert_equal(QE.韻目到韻('敬'), '庚')
assert_equal(QE.韻目到韻('東'), '東')
