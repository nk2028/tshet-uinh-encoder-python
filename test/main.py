from QieyunEncoder import encode, decode
from os import path

here = path.abspath(path.dirname(__file__))

seen = set()

def roundtrip(母, 呼, 等, 重紐, 韻, 聲):
    encoded = encode(母, 呼, 等, 重紐, 韻, 聲)
    assert encoded not in seen
    seen.add(encoded)
    decoded = decode(encoded)
    assert decoded == (母, 呼, 等, 重紐, 韻, 聲)

def test():
    with open(path.join(here, 'examples.txt'), encoding='utf8') as f:
        next(f) # skip header
        for line in f:
            母, 呼, 等, 重紐, 韻, 聲 = line.rstrip('\n').split(',')
            if 呼 == '': 呼 = None
            if 重紐 == '': 重紐 = None
            roundtrip(母, 呼, 等, 重紐, 韻, 聲)
