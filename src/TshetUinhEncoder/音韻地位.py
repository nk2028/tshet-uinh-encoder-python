# -*- coding: utf-8 -*-

import re

from . import 常量
from ._母對應的標準等 import 母對應的標準等
from .轉換 import 母到清濁, 母到音, 母到組, 韻到攝, 母與等到類

編碼表 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
韻順序表 = '東_冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢真臻文殷元魂痕寒刪山仙先蕭宵肴豪歌_麻_陽唐庚_耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'
解析音韻描述 = re.compile(fr'([{常量.所有母}])([{常量.所有呼}])?([{常量.所有等}])?([{常量.所有重紐}])?([{常量.所有韻}])([{常量.所有聲}])')

class 音韻地位:
    '''
    切韻音系音韻地位。

    :param 母: 聲母
    :type 母: str
    :param 呼: 呼（開/合），可以爲 ``None``
    :type 呼: str, optional
    :param 等: 等
    :type 等: str
    :param 重紐: 重紐，可以爲 ``None``
    :type 重紐: str, optional
    :param 韻: 韻
    :type 韻: str
    :param 聲: 聲調
    :type 聲: str
    '''

    def __init__(self, 母: str, 呼: str | None, 等: str, 重紐: str | None, 韻: str, 聲: str):
        韻 = 韻.replace('欣', '殷').replace('眞', '真')  # 容錯

        音韻地位.驗證(母, 呼, 等, 重紐, 韻, 聲)

        self.母 = 母
        self.呼 = 呼
        self.等 = 等
        self.重紐 = 重紐
        self.韻 = 韻
        self.聲 = 聲

    @property
    def 清濁(self) -> str:
        '''
        清濁（全清、次清、全濁、次濁）。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').清濁
            '全清'
            >>> 音韻地位.from描述('羣開三A支平').清濁
            '全濁'
        '''
        return 母到清濁(self.母)

    @property
    def 音(self) -> str:
        '''
        音（脣音、舌音、齒音、牙音、喉音）。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').音
            '脣'
            >>> 音韻地位.from描述('羣開三A支平').音
            '牙'
        '''
        return 母到音(self.母)

    @property
    def 組(self) -> str | None:
        '''
        組。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').組
            '幫'
            >>> 音韻地位.from描述('羣開三A支平').組
            '見'
        '''
        return 母到組(self.母)

    @property
    def 攝(self) -> str:
        '''
        攝。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').攝
            '咸'
            >>> 音韻地位.from描述('羣開三A支平').攝
            '止'
        '''
        return 韻到攝(self.韻)

    @property
    def 類(self) -> str:
        '''
        五十一聲類。

        注意五十一聲類中俟母獨立，故實為五十二個。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').類
            '方'
            >>> 音韻地位.from描述('羣開三A支平').類
            '渠'
        '''
        return 母與等到類(self.母, self.等)

    @property
    def 描述(self) -> str:
        '''
        音韻描述。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').描述
            '幫三凡入'
            >>> 音韻地位.from描述('羣開三A支平').描述
            '羣開三A支平'
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲

        return 母 + (呼 or '') + 等 + (重紐 or '') + 韻 + 聲

    @property
    def 最簡描述(self) -> str:
        '''
        最簡音韻描述。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').最簡描述
            '幫凡入'
            >>> 音韻地位.from描述('羣開三A支平').最簡描述
            '羣開A支平'
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲

        if 韻 not in 常量.開合兼備的韻:
            呼 = ''
        if 韻 not in 常量.一三等韻 and 韻 not in 常量.二三等韻:
            等 = ''
        if 重紐 is None:
            重紐 = ''

        return f'{母}{呼}{等}{重紐}{韻}{聲}'

    @property
    def 表達式(self) -> str:
        '''
        音韻表達式。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').表達式
            '幫母 三等 凡韻 入聲'
            >>> 音韻地位.from描述('羣開三A支平').表達式
            '羣母 開口 三等 重紐A類 支韻 平聲'
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲

        呼字段 = f'{呼}口 ' if 呼 else ''
        重紐字段 = f'重紐{重紐}類 ' if 重紐 else ''

        return f'{母}母 {呼字段}{等}等 {重紐字段}{韻}韻 {聲}聲'

    @property
    def 最簡表達式(self) -> str:
        '''
        最簡音韻表達式。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').最簡表達式
            '幫母 凡韻 入聲'
            >>> 音韻地位.from描述('羣開三A支平').最簡表達式
            '羣母 開口 重紐A類 支韻 平聲'
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲

        if 韻 not in 常量.開合兼備的韻:
            呼 = None
        if 韻 not in 常量.一三等韻 and 韻 not in 常量.二三等韻:
            等 = ''

        呼字段 = f'{呼}口 ' if 呼 else ''
        等字段 = f'{等}等 ' if 等 else ''
        重紐字段 = f'重紐{重紐}類 ' if 重紐 else ''
        韻字段 = f'{韻}韻 ' if 韻 else ''

        return f'{母}母 {呼字段}{等字段}{重紐字段}{韻字段}{聲}聲'

    @property
    def 編碼(self) -> str:
        '''
        音韻編碼。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').編碼
            'A9D'
            >>> 音韻地位.from描述('羣開三A支平').編碼
            'fFA'
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲

        母編碼 = 常量.所有母.index(母)

        韻編碼 = {
            '東三': 1,
            '歌三': 38,
            '麻三': 40,
            '庚三': 44,
        }.get(韻 + 等) or 韻順序表.index(韻)

        其他編碼 = ((呼 == '合') << 3) + ((重紐 == 'B') << 2) + 常量.所有聲.index(聲)

        return 編碼表[母編碼] + 編碼表[韻編碼] + 編碼表[其他編碼]

    def 屬於(self, 表達式: str) -> bool:
        '''
        判斷音韻地位是否符合給定的音韻表達式。

        Examples:

            >>> 音韻地位.from描述('幫三凡入').屬於('章母')
            False
            >>> 音韻地位.from描述('幫三凡入').屬於('一四等')
            False
            >>> 音韻地位.from描述('幫三凡入').屬於('幫組 或 陽韻')
            True
        '''
        def inner(q: str):
            if q.endswith('母'):
                母們 = q[:-1]
                assert len(母們) > 0, '未指定母'
                for 母 in 母們:
                    assert 母 in 常量.所有母, 母 + '母不存在'
                return self.母 in 母們

            if q.endswith('等'):
                等們 = q[:-1]
                assert len(等們) > 0, '未指定等'
                for 等 in 等們:
                    assert 等 in '一二三四', 等 + '等不存在'
                return self.等 in 等們

            if q.endswith('韻'):
                韻們 = q[:-1]
                assert len(韻們) > 0, '未指定韻'
                for 韻 in 韻們:
                    assert 韻 in 常量.所有韻, 韻 + '韻不存在'
                return self.韻 in 韻們

            if q.endswith('聲'):
                聲們 = q[:-1]
                assert len(聲們) > 0, '未指定聲'

                def equal聲(聲: str) -> bool:
                    if 聲 in '平上去入':
                        return self.聲 == 聲
                    if 聲 == '仄':
                        return self.聲 != '平'
                    if 聲 == '舒':
                        return self.聲 != '入'
                    raise AssertionError(聲 + '聲不存在')
                return any(equal聲(聲) for 聲 in 聲們)

            if q.endswith('組'):
                組們 = q[:-1]
                assert len(組們) > 0, '未指定組'
                # TODO: 所有組
                # for 組 in 組們:
                #     assert 組 in 所有組, 組 + '組不存在'
                return self.組 is not None and self.組 in 組們

            if q.endswith('音'):
                音們 = q[:-1]
                assert len(音們) > 0, '未指定音'
                for 音 in 音們:
                    assert 音 in '脣舌牙齒喉', 音 + '音不存在'
                return self.音 in 音們

            if q.endswith('攝'):
                攝們 = q[:-1]
                assert len(攝們) > 0, '未指定攝'
                # TODO: 所有攝
                # for 攝 in 攝們:
                #     assert 攝 in 所有攝, 攝 + '攝不存在'
                return self.攝 in 攝們

            if q == '開口':
                return self.呼 == '開'
            if q == '合口':
                return self.呼 == '合'
            if q == '開合中立':
                return self.呼 is None
            if q == '重紐A類':
                return self.重紐 == 'A'
            if q == '重紐B類':
                return self.重紐 == 'B'
            if q == '全清':
                return self.清濁 == '全清'
            if q == '次清':
                return self.清濁 == '次清'
            if q == '全濁':
                return self.清濁 == '全濁'
            if q == '次濁':
                return self.清濁 == '次濁'

            raise AssertionError('無此運算符：' + q)

        return any(all(inner(q) for q in p.split(' ')) for p in 表達式.split(' 或 '))

    @staticmethod
    def 驗證(母: str, 呼: str | None, 等: str, 重紐: str | None, 韻: str, 聲: str):
        '''
        驗證給定的音韻地位六要素是否合法。

        :param 母: 聲母
        :type 母: str
        :param 呼: 呼（開口呼/合口呼），可以爲 ``None``
        :type 呼: str, optional
        :param 等: 等
        :type 等: str
        :param 重紐: 重紐，可以爲 ``None``
        :type 重紐: str, optional
        :param 韻: 韻
        :type 韻: str
        :param 聲: 聲調
        :type 聲: str
        '''

        assert len(母) == 1 and 母 in 常量.所有母, 'Unexpected 母: ' + repr(母)
        assert len(等) == 1 and 等 in 常量.所有等, 'Unexpected 等: ' + repr(等)
        assert len(韻) == 1 and 韻 in 常量.所有韻, 'Unexpected 韻: ' + repr(韻)
        assert len(聲) == 1 and 聲 in 常量.所有聲, 'Unexpected 聲: ' + repr(聲)

        if 母 in '幫滂並明' or 韻 in 常量.開合中立的韻:
            assert 呼 is None, 'Unexpected 呼: ' + repr(呼)
        elif 韻 in 常量.必爲開口的韻:
            assert 呼 == '開'
        elif 韻 in 常量.必爲合口的韻:
            assert 呼 == '合'
        else:
            assert 呼 is not None and len(呼) == 1 and 呼 in 常量.所有呼, 'Unexpected 呼: ' + repr(呼)

        if 母 in 常量.重紐母 and 韻 in 常量.重紐韻:
            assert 重紐 is not None and len(重紐) == 1 and 重紐 in 常量.所有重紐, 'Unexpected 重紐: ' + repr(重紐)
        else:
            assert 重紐 is None, 'Unexpected 重紐: ' + repr(重紐)

        if 韻 in 常量.一等韻:
            assert 等 == '一', 'Unexpected 等: ' + repr(等)
        elif 韻 in 常量.二等韻:
            assert 等 == '二', 'Unexpected 等: ' + repr(等)
        elif 韻 in 常量.三等韻:
            assert 等 == '三', 'Unexpected 等: ' + repr(等)
        elif 韻 in 常量.四等韻:
            assert 等 == '四', 'Unexpected 等: ' + repr(等)
        elif 韻 in 常量.一三等韻:
            assert 等 in '一三', 'Unexpected 等: ' + repr(等)
        elif 韻 in 常量.二三等韻:
            assert 等 in '二三', 'Unexpected 等: ' + repr(等)

    @staticmethod
    def from編碼(編碼: str):
        '''
        將音韻編碼轉換爲音韻地位。
        '''
        assert len(編碼) == 3, 'Invalid 編碼: ' + repr(編碼)

        母編碼 = 編碼表.index(編碼[0])
        韻編碼 = 編碼表.index(編碼[1])
        其他編碼 = 編碼表.index(編碼[2])

        呼編碼 = 其他編碼 >> 3
        重紐編碼 = (其他編碼 >> 2) & 0b1
        聲編碼 = 其他編碼 & 0b11

        母 = 常量.所有母[母編碼]
        呼: str | None = 常量.所有呼[呼編碼]
        重紐: str | None = 常量.所有重紐[重紐編碼]
        聲 = 常量.所有聲[聲編碼]

        match 韻編碼:
            case 0:
                韻 = '東'
                等 = '一'
            case 1:
                韻 = '東'
                等 = '三'
            case 37:
                韻 = '歌'
                等 = '一'
            case 38:
                韻 = '歌'
                等 = '三'
            case 39:
                韻 = '麻'
                等 = '二'
            case 40:
                韻 = '麻'
                等 = '三'
            case 43:
                韻 = '庚'
                等 = '二'
            case 44:
                韻 = '庚'
                等 = '三'
            case _:
                韻 = 韻順序表[韻編碼]
                if 韻 in 常量.一等韻:
                    等 = '一'
                elif 韻 in 常量.二等韻:
                    等 = '二'
                elif 韻 in 常量.三等韻:
                    等 = '三'
                elif 韻 in 常量.四等韻:
                    等 = '四'

        if 母 in '幫滂並明' or 韻 in 常量.開合中立的韻:
            assert 呼 == '開'
            呼 = None

        if 母 not in 常量.重紐母 or 韻 not in 常量.重紐韻:
            assert 重紐 == 'A'
            重紐 = None

        音韻地位.驗證(母, 呼, 等, 重紐, 韻, 聲)

        return 音韻地位(母, 呼, 等, 重紐, 韻, 聲)

    @staticmethod
    def from描述(描述: str):
        '''
        將音韻描述或最簡音韻描述轉換爲音韻地位。
        '''
        # TODO: 重寫解析器，支援更多格式

        描述 = 描述.replace('欣', '殷').replace('眞', '真')  # 容錯

        match = 解析音韻描述.fullmatch(描述)
        assert match is not None, 'Invalid 描述: ' + repr(描述)

        母, 呼, 等, 重紐, 韻, 聲 = match.groups()

        if 呼 is None and 母 not in '幫滂並明':
            if 韻 in 常量.必爲開口的韻:
                呼 = '開'
            elif 韻 in 常量.必爲合口的韻:
                呼 = '合'

        if 等 is None:
            if 韻 in 常量.一等韻:
                等 = '一'
            elif 韻 in 常量.二等韻:
                等 = '二'
            elif 韻 in 常量.三等韻:
                等 = '三'
            elif 韻 in 常量.四等韻:
                等 = '四'
            else:
                raise ValueError(f'Unexpected 韻: {韻}')

        音韻地位.驗證(母, 呼, 等, 重紐, 韻, 聲)

        return 音韻地位(母, 呼, 等, 重紐, 韻, 聲)

    def is_normal(self):
        '''
        是 normal 的音韻地位。

        例如，端母二等不是 normal 的音韻地位。
        '''
        return self.等 in 母對應的標準等[self.母]

    def __repr__(self) -> str:
        return '<音韻地位 ' + self.描述 + '>'

    def __eq__(self, that) -> bool:
        if not isinstance(that, 音韻地位):
            return False
        return self.最簡描述 == that.最簡描述

    def __lt__(self, that) -> bool:
        if not isinstance(that, 音韻地位):
            raise TypeError("'<' not supported between instances of '音韻地位' and " + type(that).__name__)

        def 母到編碼(母):
            return 常量.所有母.index(母)

        def 呼到編碼(呼):
            return [None, '開', '合'].index(呼)

        def 等到編碼(等):
            return '一二三四'.index(等)

        def 重紐到編碼(重紐):
            return [None, 'A', 'B'].index(重紐)

        def 韻到編碼(韻):
            return 常量.所有韻.index(韻)

        def 聲到編碼(聲):
            return 常量.所有聲.index(聲)

        return (聲到編碼(self.聲), 韻到編碼(self.韻), 重紐到編碼(self.重紐), 等到編碼(self.等), 呼到編碼(self.呼), 母到編碼(self.母)) \
             < (聲到編碼(that.聲), 韻到編碼(that.韻), 重紐到編碼(that.重紐), 等到編碼(that.等), 呼到編碼(that.呼), 母到編碼(that.母))

    def __le__(self, that) -> bool:
        if not isinstance(that, 音韻地位):
            raise TypeError("'<' not supported between instances of '音韻地位' and " + type(that).__name__)
        return self == that or self < that

    def __hash__(self) -> int:
        return hash(self.最簡描述)
