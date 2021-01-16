# qieyun-encoder [![](https://badge.fury.io/py/qieyun-encoder.svg)](https://pypi.org/project/qieyun-encoder/) ![](https://github.com/nk2028/qieyun-encoder/workflows/Python%20package/badge.svg)

Convert a phonological position of the Qieyun phonological system to the three-character phonological encoding and the phonological description.

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
>>> QieyunEncoder.to描述('端', None, '一', None, '東', '平')
'端一東平'
>>> QieyunEncoder.from描述('端一東平')
('端', None, '一', None, '東', '平')
```
