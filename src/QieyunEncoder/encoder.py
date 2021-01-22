# -*- coding: utf-8 -*-

import re
from typing import Optional

編碼表 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

所有母 = '幫滂並明端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日見溪羣疑影曉匣云以'
所有呼 = '開合'
所有等 = '一二三四'
所有重紐 = 'AB'
所有韻 = '東冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢眞臻文欣元魂痕寒刪山仙先蕭宵肴豪歌麻陽唐庚耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'
所有聲 = '平上去入'

重紐母 = '幫滂並明見溪羣疑影曉'
重紐韻 = '支脂祭眞仙宵清侵鹽'

開合皆有的韻 = '支脂微齊祭泰佳皆夬廢眞元寒刪山仙先歌麻陽唐庚耕清青蒸登'
必為開口的韻 = '咍痕欣嚴之魚臻蕭宵肴豪侯侵覃談鹽添咸銜'
必為合口的韻 = '灰魂文凡'
開合中立的韻 = '東冬鍾江虞模尤幽'

韻順序表 = '東_冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢眞臻文欣元魂痕寒刪山仙先蕭宵肴豪歌_麻_陽唐庚_耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'

一等韻 = '冬模泰咍灰痕魂寒豪唐登侯覃談'
二等韻 = '江佳皆夬刪山肴耕咸銜'
三等韻 = '鍾支脂之微魚虞祭廢眞臻欣元文仙宵陽清蒸尤幽侵鹽嚴凡'
四等韻 = '齊先蕭青添'
一三等韻 = '東歌'
二三等韻 = '麻庚'

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

	if 韻 in 一等韻:
		assert 等 == '一', 'Unexpected 等: ' + repr(等)
	elif 韻 in 二等韻:
		assert 等 == '二', 'Unexpected 等: ' + repr(等)
	elif 韻 in 三等韻:
		assert 等 == '三', 'Unexpected 等: ' + repr(等)
	elif 韻 in 四等韻:
		assert 等 == '四', 'Unexpected 等: ' + repr(等)
	elif 韻 in 一三等韻:
		assert 等 in ('一', '三'), 'Unexpected 等: ' + repr(等)
	elif 韻 in 二三等韻:
		assert 等 in ('二', '三'), 'Unexpected 等: ' + repr(等)

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

	if 韻 == '東' and 等 == '一':
		韻編碼 = 0
	elif 韻 == '東' and 等 == '三':
		韻編碼 = 1
	elif 韻 == '歌' and 等 == '一':
		韻編碼 = 37
	elif 韻 == '歌' and 等 == '三':
		韻編碼 = 38
	elif 韻 == '麻' and 等 == '二':
		韻編碼 = 39
	elif 韻 == '麻' and 等 == '三':
		韻編碼 = 40
	elif 韻 == '庚' and 等 == '二':
		韻編碼 = 43
	elif 韻 == '庚' and 等 == '三':
		韻編碼 = 44
	else:
		韻編碼 = 韻順序表.index(韻)

	其他編碼 = ((呼 == '合') << 3) + ((重紐 == 'B') << 2) + (所有聲.index(聲))

	return 編碼表[母編碼] + 編碼表[韻編碼] + 編碼表[其他編碼]

def from編碼(s: str):
	'''
	將音韻編碼轉換為音韻地位六要素。
	```
	>>> from編碼('EAA')
	('端', None, '一', None, '東', '平')
	```
	'''
	assert len(s) == 3, 'Invalid 編碼: ' + repr(s)

	母編碼 = 編碼表.index(s[0])
	韻編碼 = 編碼表.index(s[1])
	其他編碼 = 編碼表.index(s[2])

	呼編碼 = 其他編碼 >> 3
	重紐編碼 = (其他編碼 >> 2) & 0b1
	聲編碼 = 其他編碼 & 0b11

	母 = 所有母[母編碼]
	呼 = 所有呼[呼編碼]
	重紐 = 所有重紐[重紐編碼]
	聲 = 所有聲[聲編碼]

	if 韻編碼 == 0:
		韻 = '東'; 等 = '一'
	elif 韻編碼 == 1:
		韻 = '東'; 等 = '三'
	elif 韻編碼 == 37:
		韻 = '歌'; 等 = '一'
	elif 韻編碼 == 38:
		韻 = '歌'; 等 = '三'
	elif 韻編碼 == 39:
		韻 = '麻'; 等 = '二'
	elif 韻編碼 == 40:
		韻 = '麻'; 等 = '三'
	elif 韻編碼 == 43:
		韻 = '庚'; 等 = '二'
	elif 韻編碼 == 44:
		韻 = '庚'; 等 = '三'
	else:
		韻 = 韻順序表[韻編碼]
		if 韻 in 一等韻:
			等 = '一'
		elif 韻 in 二等韻:
			等 = '二'
		elif 韻 in 三等韻:
			等 = '三'
		elif 韻 in 四等韻:
			等 = '四'

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
