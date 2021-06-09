# -*- coding: utf-8 -*-

from typing import Optional, Union

from .工具.韻目到韻 import 韻目到韻
from .常量 import 常量

_韻鏡母位置表 = [
    '脣音第一位', '脣音第二位', '脣音第三位', '脣音第四位',
    '舌音第一位', '舌音第二位', '舌音第三位', '舌音第四位',
    '牙音第一位', '牙音第二位', '牙音第三位', '牙音第四位',
    '齒音第一位', '齒音第二位', '齒音第三位', '齒音第四位', '齒音第五位',
    '喉音第一位', '喉音第二位', '喉音第三位', '喉音第四位',
    '舌齒音第一位', '舌齒音第二位',
]

_d韻鏡母位置2韻鏡母號 = {韻鏡母位置: 韻鏡母號 for 韻鏡母號, 韻鏡母位置 in enumerate(_韻鏡母位置表)}

_韻鏡母表 = [
    '幫非', '滂敷', '並奉', '明微',
    '端知', '透徹', '定澄', '泥孃',
    '見', '溪', '羣', '疑',
    '精照', '清穿', '從牀', '心審', '邪禪',
    '影', '曉', '匣', '喻',
    '來', '日',
]

_d韻鏡母2韻鏡母號 = {}

for 韻鏡母號, 韻鏡母 in enumerate(_韻鏡母表):
    _d韻鏡母2韻鏡母號[韻鏡母] = 韻鏡母號
    if len(韻鏡母) > 1:
        for 韻鏡母單字 in 韻鏡母:
            _d韻鏡母2韻鏡母號[韻鏡母單字] = 韻鏡母號


class 韻鏡位置:
    '''
    韻鏡位置。
    '''

    def __init__(self, 韻鏡母: Union[str, int], 韻鏡開合: Optional[str], 韻鏡等: str, 韻: str, 聲: str) -> None:
        # normalize 母
        # - 韻鏡母號（0-22，從右至左計數）
        # - 韻鏡母位置（脣音第一位，etc）
        # - 韻鏡母
        #     - 精照，etc
        #     - 精，照，etc
        韻鏡母號 = _d韻鏡母位置2韻鏡母號.get(韻鏡母, _d韻鏡母2韻鏡母號.get(韻鏡母))
        if 韻鏡母號 is not None:
            self.韻鏡母號 = 韻鏡母號
        else:
            assert isinstance(韻鏡母, int), 'Unexpected 韻鏡母: ' + repr(韻鏡母)
            self.韻鏡母號 = 韻鏡母

        # normalize 開合
        # - 韻鏡轉號
        # - 韻鏡開合（開、合、None）
        self.韻鏡開合 = 韻鏡開合

        self.韻鏡等 = 韻鏡等

        # normalize 韻
        self.韻 = 韻目到韻(韻)

        self.聲 = 聲

    @property
    def 韻鏡母(self) -> str:
        return _韻鏡母表[self.韻鏡母號]

    @property
    def 最簡韻鏡母(self) -> str:
        韻鏡母號 = self.韻鏡母號
        韻鏡母 = self.韻鏡母

        if 0 <= 韻鏡母號 < 4:  # 幫非組
            return 韻鏡母[self.韻鏡等 == '三' and self.韻 in 常量.輕脣韻]
        if 4 <= 韻鏡母號 < 8 or 12 <= 韻鏡母號 < 17:  # 端知組、精照組
            return 韻鏡母[self.韻鏡等 in '二三']
        return 韻鏡母

    @property
    def 描述(self) -> str:
        return self.最簡韻鏡母 + (self.韻鏡開合 or '') + self.韻鏡等 + self.韻 + self.聲

    def __repr__(self) -> str:
        return f'<韻鏡位置 {self.描述}>'

    def __eq__(self, that) -> bool:
        if not isinstance(that, 韻鏡位置):
            return False
        return self.描述 == that.描述

    def __hash__(self) -> int:
        return hash(self.描述)
