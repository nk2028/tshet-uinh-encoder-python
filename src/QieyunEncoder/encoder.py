# -*- coding: utf-8 -*-

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

def validate(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
	'''
	驗證給定的音韻地位六要素是否合法。
	'''
	assert len(母) == 1 and 母 in 所有母, 'Unexpected 母: ' + repr(母)
	assert len(等) == 1 and 等 in 所有等, 'Unexpected 等: ' + repr(等)
	assert len(韻) == 1 and 韻 in 所有韻, 'Unexpected 韻: ' + repr(韻)
	assert len(聲) == 1 and 聲 in 所有聲, 'Unexpected 聲: ' + repr(聲)

	if 母 in '幫滂並明' or 韻 == '模':
		assert 呼 is None
	else:
		assert len(呼) == 1 and 呼 in 所有呼

	if 母 in 重紐母 and 韻 in 重紐韻:
		assert len(重紐) == 1 and 重紐 in 所有重紐
	else:
		assert 重紐 is None

def encode(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
	'''
	將音韻地位六要素轉換為音韻編碼。
	```
	>>> encode('端', '開', '一', None, '東', '平')
	'EAA'
	```
	'''
	validate(母, 呼, 等, 重紐, 韻, 聲)

	母編碼 = 所有母.index(母)
	韻編碼 = 所有韻.index(韻)
	其他編碼 = ((呼 == '合') << 5) + (所有等.index(等) << 3) + ((重紐 == 'B') << 2) + (所有聲.index(聲))

	return 編碼表[母編碼] + 編碼表[韻編碼] + 編碼表[其他編碼]

def decode(s: str):
	'''
	將音韻編碼轉換為音韻地位六要素。
	```
	>>> decode('EAA')
	('端', '開', '一', None, '東', '平')
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

	if 母 in '幫滂並明' or 韻 == '模':
		assert 呼 == '開'
		呼 = None

	if 母 not in 重紐母 or 韻 not in 重紐韻:
		assert 重紐 == 'A'
		重紐 = None

	return 母, 呼, 等, 重紐, 韻, 聲
