# qieyun-encoder [![](https://badge.fury.io/py/qieyun-encoder.svg)](https://pypi.org/project/qieyun-encoder/) ![](https://github.com/nk2028/qieyun-encoder/workflows/Python%20package/badge.svg)

《切韻》音系音韻地位編碼器

Note: this package is only intended for developers.

## Introduction

將一個《切韻》音系音韻地位轉換為三個字符的編碼。

## Install

```sh
$ pip install qieyun-encoder
```

## Usage

```python
>>> from QieyunEncoder import encode, decode
>>> encode('端', '開', '一', None, '東', '平')
'EAA'
>>> decode('EAA')
('端', '開', '一', None, '東', '平')
```
