# -*- coding: utf-8 -*-

import re
from typing import Optional

編碼表 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-'
所有母 = '幫滂並明端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日見溪羣疑影曉匣云以'
所有呼 = '開合'
所有等 = '一二三四'
所有重紐 = 'AB'
所有韻 = '東冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢眞臻文欣元魂痕寒刪山仙先蕭宵肴豪歌麻陽唐庚耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'
所有聲 = '平上去入'
重紐母 = '幫滂並明見溪羣疑影曉'
重紐韻 = '支脂祭眞仙宵清侵鹽'
必為開口的韻 = '咍痕欣嚴之魚臻蕭宵肴豪侯侵覃談鹽添咸銜'
必為合口的韻 = '灰魂文凡'
開合中立的韻 = '東冬鍾江虞模尤幽'

def 驗證(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
	'''
	驗證給定的音韻地位六要素是否合法。
	'''
	assert len(母) == 1 and 母 in 所有母, 'Unexpected 母: ' + repr(母)
	assert len(等) == 1 and 等 in 所有等, 'Unexpected 等: ' + repr(等)
	assert len(韻) == 1 and 韻 in 所有韻, 'Unexpected 韻: ' + repr(韻)
	assert len(聲) == 1 and 聲 in 所有聲, 'Unexpected 聲: ' + repr(聲)

	if 母 in '幫滂並明' or 韻 in 開合中立的韻:
		assert 呼 is None, 'Unexpected 呼: ' + repr(呼)
	elif 韻 in 必為開口的韻:
		assert 呼 == '開'
	elif 韻 in 必為合口的韻:
		assert 呼 == '合'
	else:
		assert 呼 is not None and len(呼) == 1 and 呼 in 所有呼, 'Unexpected 呼: ' + repr(呼)

	if 母 in 重紐母 and 韻 in 重紐韻:
		assert 重紐 is not None and len(重紐) == 1 and 重紐 in 所有重紐, 'Unexpected 重紐: ' + repr(重紐)
	else:
		assert 重紐 is None, 'Unexpected 重紐: ' + repr(重紐)

def to編碼(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
	'''
	將音韻地位六要素轉換為音韻編碼。
	```
	>>> to編碼('端', None, '一', None, '東', '平')
	'EAA'
	```
	'''
	驗證(母, 呼, 等, 重紐, 韻, 聲)

	母編碼 = 所有母.index(母)
	韻編碼 = 所有韻.index(韻)
	其他編碼 = ((呼 == '合') << 5) + (所有等.index(等) << 3) + ((重紐 == 'B') << 2) + (所有聲.index(聲))

	return 編碼表[母編碼] + 編碼表[韻編碼] + 編碼表[其他編碼]

def from編碼(s: str):
	'''
	將音韻編碼轉換為音韻地位六要素。
	```
	>>> from編碼('EAA')
	('端', None, '一', None, '東', '平')
	```
	'''
	母編碼 = 編碼表.index(s[0])
	韻編碼 = 編碼表.index(s[1])
	其他編碼 = 編碼表.index(s[2])

	呼編碼 = 其他編碼 >> 5
	等編碼 = (其他編碼 >> 3) & 0b11
	重紐編碼 = (其他編碼 >> 2) & 0b1
	聲編碼 = 其他編碼 & 0b11

	母 = 所有母[母編碼]
	韻 = 所有韻[韻編碼]
	呼 = 所有呼[呼編碼]
	等 = 所有等[等編碼]
	重紐 = 所有重紐[重紐編碼]
	聲 = 所有聲[聲編碼]

	if 母 in '幫滂並明' or 韻 in 開合中立的韻:
		assert 呼 == '開'
		呼 = None

	if 母 not in 重紐母 or 韻 not in 重紐韻:
		assert 重紐 == 'A'
		重紐 = None

	驗證(母, 呼, 等, 重紐, 韻, 聲)

	return 母, 呼, 等, 重紐, 韻, 聲

def to描述(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
	'''
	將音韻地位六要素轉換為音韻描述。
	```
	>>> to描述('端', None, '一', None, '東', '平')
	'端一東平'
	```
	'''
	驗證(母, 呼, 等, 重紐, 韻, 聲)

	return 母 + (呼 or '') + 等 + (重紐 or '') + 韻 + 聲

pattern = re.compile('([%s])([%s]?)([%s])([%s]?)([%s])([%s])' % (所有母, 所有呼, 所有等, 所有重紐, 所有韻, 所有聲))

def from描述(s: str):
	'''
	將音韻描述轉換為音韻地位六要素。
	```
	>>> from描述('端一東平')
	('端', None, '一', None, '東', '平')
	```
	'''
	match = pattern.fullmatch(s)
	assert match is not None

	母 = match.group(1)
	呼 = match.group(2) or None
	等 = match.group(3)
	重紐 = match.group(4) or None
	韻 = match.group(5)
	聲 = match.group(6)

	驗證(母, 呼, 等, 重紐, 韻, 聲)

	return 母, 呼, 等, 重紐, 韻, 聲
