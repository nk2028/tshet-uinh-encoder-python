# qieyun-encoder ![](https://github.com/nk2028/qieyun-encoder/workflows/Python%20package/badge.svg)

《切韻》音韻地位編碼器

Note: this package is only intended for developers.

## Install

```sh
$ pip install QieyunEncoder
```

## Usage

```python
>>> from QieyunEncoder import encode, decode
>>> encode('端', '開', '一', None, '東', '平')
'EAA'
>>> decode('EAA')
('端', '開', '一', None, '東', '平')
```
