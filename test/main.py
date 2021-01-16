from os import path
import QieyunEncoder

here = path.abspath(path.dirname(__file__))

seen = set()

def roundtrip(母, 呼, 等, 重紐, 韻, 聲):
	'''
	將音韻地位六要素轉換為音韻編碼，再將音韻編碼轉換為音韻地位六要素。

	用於測試轉換是否出現異常，以及轉換結果與轉換前是否一致。
	'''
	encoded = QieyunEncoder.to編碼(母, 呼, 等, 重紐, 韻, 聲)
	assert encoded not in seen
	seen.add(encoded)
	decoded = QieyunEncoder.from編碼(encoded)
	assert decoded == (母, 呼, 等, 重紐, 韻, 聲)

def test():
	'''
	執行測試。
	'''
	with open(path.join(here, 'examples.txt'), encoding='utf8') as f:
		next(f) # skip header
		for line in f:
			母, 呼, 等, 重紐, 韻, 聲 = line.rstrip('\n').split(',')
			if 呼 == '': 呼 = None
			if 重紐 == '': 重紐 = None
			roundtrip(母, 呼, 等, 重紐, 韻, 聲)
