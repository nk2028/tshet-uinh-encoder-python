# qieyun-encoder [![](https://badge.fury.io/py/qieyun-encoder.svg)](https://pypi.org/project/qieyun-encoder/) ![](https://github.com/nk2028/qieyun-encoder/workflows/Python%20package/badge.svg)

Convert a pronunciation in the Qieyun phonological system to a three-character phonological encoding.

Note: this package is only intended for developers.

## Install

```sh
$ pip install qieyun-encoder
```

## Usage

```python
>>> import QieyunEncoder
>>> QieyunEncoder.to編碼('端', None, '一', None, '東', '平')
'EAA'
>>> QieyunEncoder.from編碼('EAA')
('端', None, '一', None, '東', '平')
```
