# -*- coding: utf-8 -*-

'''
將音韻屬性轉換爲韻鏡位置。
'''

from ..韻鏡位置 import 韻鏡位置
from ..常量 import 常量
from .韻目到韻 import 韻目到韻
from .母到組 import 母到組


def 音韻屬性到韻鏡位置們(母: str, 韻目: str, 聲: str):
    raise NotImplementedError

