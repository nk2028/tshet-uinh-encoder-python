# -*- coding: utf-8 -*-

'''
切韻音系音韻地位及相關操作。

## 音韻屬性

### 母、音、組、清濁

母採用三十八聲類的分類方法。

<style>
.big-table { border-collapse: collapse; margin: 1em 0; display: block; }
.big-table th, .big-table td { border: 1px solid; padding: 4px 6px; text-align: center; }
.admonition { border-radius: 14px; padding: 2px 18px !important; }
.admonition > .admonition-title { display: none; }
</style>

<table class="big-table">
<tbody>
<tr><th></th><th>全清</th><th>次清</th><th>全濁</th><th>次濁</th><th>全清</th><th>全濁</th></tr>
<tr><th>脣音</th><td>幫</td><td>滂</td><td>並</td><td>明</td><td></td><td></td></tr>
<tr><th rowspan="3">舌音</th><td>端</td><td>透</td><td>定</td><td>泥</td><td></td><td></td></tr>
<tr><td>知</td><td>徹</td><td>澄</td><td>孃</td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td>來</td><td></td><td></td></tr>
<tr><th rowspan="4">齒音</th><td>精</td><td>清</td><td>從</td><td></td><td>心</td><td>邪</td></tr>
<tr><td>莊</td><td>初</td><td>崇</td><td></td><td>生</td><td>俟</td></tr>
<tr><td>章</td><td>昌</td><td>常</td><td></td><td>書</td><td>船</td></tr>
<tr><td></td><td></td><td></td><td>日</td><td></td><td></td></tr>
<tr><th>牙音</th><td>見</td><td>溪</td><td>羣</td><td>疑</td><td></td><td></td></tr>
<tr><th rowspan="2">喉音</th><td>影</td><td></td><td></td><td>云</td><td>曉</td><td>匣</td></tr>
<tr><td></td><td></td><td></td><td>以</td><td></td><td></td></tr>
</tbody>
</table>

上表中正文部分爲母，橫向爲音與組，縱向爲清濁。

注意曉母爲全清，云母爲次濁。組不涵蓋來日以母。

.. hint::

    不要與中古後期三十六字母混淆。

    中古後期三十六字母：

    <table class="big-table">
    <tbody>
    <tr><th></th><th>全清</th><th>次清</th><th>全濁</th><th>次濁</th><th>全清</th><th>全濁</th></tr>
    <tr><th rowspan="2">脣音</th><td>幫</td><td>滂</td><td>並</td><td>明</td><td></td><td></td></tr>
    <tr><td>非</td><td>敷</td><td>奉</td><td>微</td><td></td><td></td></tr>
    <tr><th rowspan="3">舌音</th><td>端</td><td>透</td><td>定</td><td>泥</td><td></td><td></td></tr>
    <tr><td>知</td><td>徹</td><td>澄</td><td>孃</td><td></td><td></td></tr>
    <tr><td></td><td></td><td></td><td>來</td><td></td><td></td></tr>
    <tr><th rowspan="3">齒音</th><td>精</td><td>清</td><td>從</td><td></td><td>心</td><td>邪</td></tr>
    <tr><td>照</td><td>穿</td><td>牀</td><td></td><td>審</td><td>禪</td></tr>
    <tr><td></td><td></td><td></td><td>日</td><td></td><td></td></tr>
    <tr><th>牙音</th><td>見</td><td>溪</td><td>羣</td><td>疑</td><td></td><td></td></tr>
    <tr><th>喉音</th><td>影</td><td></td><td></td><td>喻</td><td>曉</td><td>匣</td></tr>
    </tbody>
    </table>

    區別如下：

    - 幫滂並明在三等輕脣韻前分化爲非敷奉微
    - 云以母合流爲喻母
    - 莊章組合流爲照組

### 呼

取值：開、合、`None`。其中 `None` 表示開合中立。

脣音的開合必爲 `None`。

韻與開合的關係如下：

- 開合兼備的韻：支脂微齊祭泰佳皆夬廢真元寒刪山仙先歌麻陽唐庚耕清青蒸登
- 必爲開口的韻：咍痕殷嚴之魚臻蕭宵肴豪侯侵覃談鹽添咸銜
- 必爲合口的韻：灰魂文凡
- 開合中立的韻：東冬鍾江虞模尤幽

.. hint::

    不要與韻鏡的開合混淆。

    以《韻鏡》爲例，開合有三種取值：開、合、開合。

    - 在《韻鏡》中，對脣音沒有特殊處理。而在此處，脣音的開合必爲 `None`
    - 《韻鏡》所標「開合」與此處開合中立的韻的劃分並不完全相同
    - 《韻鏡》存在誤標開合的情況，如第四轉「內轉第四開合」當爲「內轉第四開」

### 等

取值：一、二、三、四。

韻與等的關係如下：

- 一等韻：冬模泰咍灰痕魂寒豪唐登侯覃談
- 二等韻：江佳皆夬刪山肴耕咸銜
- 三等韻：鍾支脂之微魚虞祭廢真臻殷元文仙宵陽清蒸尤幽侵鹽嚴凡
- 四等韻：齊先蕭青添
- 一三等韻：東歌
- 二三等韻：麻庚

母對等沒有硬性約束條件，因爲存在「無音有字」的小韻。陳澧《切韻考》：「等之云者，當主乎韻，不當主乎聲」。

.. hint::

    不要與韻鏡的等混淆。

    - 韻鏡將重紐 A 類字置於四等，實際爲三等
    - 三等韻的莊組字列在二等
    - 三等韻的精組字列在四等
    - 三等的幽韻列在四等

### 重紐

取值：`None`、重紐A類、重紐B類。

- 重紐母：幫滂並明見溪羣疑影曉
- 重紐韻：支脂祭真仙宵清侵鹽

當聲紐不爲重紐母，或韻不爲重紐韻時，重紐必須爲 `None`。

### 韻、攝

- 通攝：東冬鍾
- 江攝：江
- 止攝：支脂之微
- 遇攝：魚虞模
- 蟹攝：齊佳皆灰咍祭泰夬廢
- 臻攝：真臻文殷魂痕
- 山攝：元寒刪山先仙
- 效攝：蕭宵肴豪
- 果攝：歌
- 假攝：麻
- 宕攝：唐陽
- 梗攝：庚耕清青
- 曾攝：登蒸
- 流攝：侯尤幽
- 深攝：侵
- 咸攝：覃談鹽添咸銜嚴凡

.. hint::

    不使用諄桓戈韻，分別併入真寒歌韻。

    使用殷韻的名稱，不使用欣韻；使用真韻的寫法，不使用眞韻。但構造函式及 `from描述` 方法具備容錯功能，會執行自動轉換。

### 聲

取值：平、上、去、入；仄、舒。

其中，仄表示上去入聲，舒表示平上去聲。
'''

import re
from typing import Optional

from .常量 import 常量
from ._母對應的標準等 import 母對應的標準等
from ._音位配列規則表 import 合法性等級, 音位配列規則表
from .工具.母到清濁 import 母到清濁
from .工具.母到組 import 母到組
from .工具.母到音 import 母到音
from .工具.韻到攝 import 韻到攝

編碼表 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
韻順序表 = '東_冬鍾江支脂之微魚虞模齊祭泰佳皆夬灰咍廢真臻文殷元魂痕寒刪山仙先蕭宵肴豪歌_麻_陽唐庚_耕清青蒸登尤侯幽侵覃談鹽添咸銜嚴凡'

解析音韻描述 = re.compile('([%s])([%s])?([%s])?([%s])?([%s])([%s])' % (
    常量.所有母, 常量.所有呼, 常量.所有等, 常量.所有重紐, 常量.所有韻, 常量.所有聲))


class 音韻地位:
    '''
    切韻音系音韻地位。
    '''

    def __init__(self, 母, 呼, 等, 重紐, 韻, 聲) -> None:
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

        ```python
        >>> 音韻地位.from描述('幫三凡入').清濁
        '全清'
        >>> 音韻地位.from描述('羣開三A支平').清濁
        '全濁'
        ```
        '''
        return 母到清濁(self.母)

    @property
    def 音(self) -> str:
        '''
        音（脣音、舌音、齒音、牙音、喉音）。

        ```python
        >>> 音韻地位.from描述('幫三凡入').音
        '脣'
        >>> 音韻地位.from描述('羣開三A支平').音
        '牙'
        ```
        '''
        return 母到音(self.母)

    @property
    def 組(self) -> Optional[str]:
        '''
        組。

        ```python
        >>> 音韻地位.from描述('幫三凡入').組
        '幫'
        >>> 音韻地位.from描述('羣開三A支平').組
        '見'
        ```
        '''
        return 母到組(self.母)

    @property
    def 攝(self) -> str:
        '''
        攝。

        ```python
        >>> 音韻地位.from描述('幫三凡入').攝
        '咸'
        >>> 音韻地位.from描述('羣開三A支平').攝
        '止'
        ```
        '''
        return 韻到攝(self.韻)

    @property
    def 描述(self) -> str:
        '''
        音韻描述。

        ```python
        >>> 音韻地位.from描述('幫三凡入').描述
        '幫三凡入'
        >>> 音韻地位.from描述('羣開三A支平').描述
        '羣開三A支平'
        ```
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

        ```python
        >>> 音韻地位.from描述('幫三凡入').最簡描述
        '幫凡入'
        >>> 音韻地位.from描述('羣開三A支平').最簡描述
        '羣開A支平'
        ```
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
            等 = None

        return 母 + (呼 or '') + (等 or '') + (重紐 or '') + 韻 + 聲

    @property
    def 表達式(self) -> str:
        '''
        音韻表達式。

        ```python
        >>> 音韻地位.from描述('幫三凡入').表達式
        '幫母 三等 凡韻 入聲'
        >>> 音韻地位.from描述('羣開三A支平').表達式
        '羣母 開口 三等 重紐A類 支韻 平聲'
        ```
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

        ```python
        >>> 音韻地位.from描述('幫三凡入').最簡表達式
        '幫母 凡韻 入聲'
        >>> 音韻地位.from描述('羣開三A支平').最簡表達式
        '羣母 開口 重紐A類 支韻 平聲'
        ```
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
            等 = None

        呼字段 = f'{呼}口 ' if 呼 else ''
        等字段 = f'{等}等 ' if 等 else ''
        重紐字段 = f'重紐{重紐}類 ' if 重紐 else ''
        韻字段 = f'{韻}韻 ' if 韻 else ''

        return f'{母}母 {呼字段}{等字段}{重紐字段}{韻字段}{聲}聲'

    @property
    def 編碼(self) -> str:
        '''
        音韻編碼。

        ```python
        >>> 音韻地位.from描述('幫三凡入').編碼
        'A9D'
        >>> 音韻地位.from描述('羣開三A支平').編碼
        'fFA'
        ```
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

        ```python
        >>> 音韻地位.from描述('幫三凡入').屬於('章母')
        False
        >>> 音韻地位.from描述('幫三凡入').屬於('一四等')
        False
        >>> 音韻地位.from描述('幫三凡入').屬於('幫組 或 陽韻')
        True
        ```
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
    def 驗證(母: str, 呼: Optional[str], 等: str, 重紐: Optional[str], 韻: str, 聲: str):
        '''
        初步驗證給定的音韻地位六要素是否合法。
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
            assert 呼 is not None and len(
                呼) == 1 and 呼 in 常量.所有呼, 'Unexpected 呼: ' + repr(呼)

        if 母 in 常量.重紐母 and 韻 in 常量.重紐韻:
            assert 重紐 is not None and len(
                重紐) == 1 and 重紐 in 常量.所有重紐, 'Unexpected 重紐: ' + repr(重紐)
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
        呼 = 常量.所有呼[呼編碼]
        重紐 = 常量.所有重紐[重紐編碼]
        聲 = 常量.所有聲[聲編碼]

        if 韻編碼 == 0:
            韻 = '東'
            等 = '一'
        elif 韻編碼 == 1:
            韻 = '東'
            等 = '三'
        elif 韻編碼 == 37:
            韻 = '歌'
            等 = '一'
        elif 韻編碼 == 38:
            韻 = '歌'
            等 = '三'
        elif 韻編碼 == 39:
            韻 = '麻'
            等 = '二'
        elif 韻編碼 == 40:
            韻 = '麻'
            等 = '三'
        elif 韻編碼 == 43:
            韻 = '庚'
            等 = '二'
        elif 韻編碼 == 44:
            韻 = '庚'
            等 = '三'
        else:
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

        音韻地位.驗證(母, 呼, 等, 重紐, 韻, 聲)

        return 音韻地位(母, 呼, 等, 重紐, 韻, 聲)

    def 合法性(self) -> tuple[str, Optional['音韻地位']]:
        '''
        聲、韻、調組合的合法性。
        如果有等價但更優的音韻地位能作爲替代，那麼也返回更優音韻地位，合法性取原地位和更優地位中的較差者。
        '''
        母 = self.母
        呼 = self.呼
        等 = self.等
        重紐 = self.重紐
        韻 = self.韻
        聲 = self.聲
        音韻地位.驗證(母, 呼, 等, 重紐, 韻, 聲)

        合法性 = 合法性等級.強合法

        類隔 = {
            '四': dict(zip('知徹澄孃莊初崇生俟云', '端透定泥精清從心邪匣')),
            '一': dict(zip('知徹澄孃莊初崇生俟云', '端透定泥精清從心邪匣')),
            '二': dict(zip('端透定泥精清從心邪云', '知徹澄孃莊初崇生俟匣')),
            '三': dict(zip('端透定泥匣', '知徹澄孃云')),
        }
        開合分韻 = dict(zip(
            '魚咍痕殷嚴',
            '虞灰魂文凡'
        ))
        銳音分韻 = dict(zip(
            # 銳音不能拼第一行韻，而第二行相應的韻是其更優音韻地位
            # 注意第一行韻不都是 C₁ 類三等韻，例外是恰恰相反的幽/尤之分
            '微廢文殷元歌幽嚴凡',
            '脂祭真真仙麻尤鹽鹽'
        ))
        莊三化二韻 = {
            # 有對應二等韻的三等韻拼莊組時以二等韻作爲更優音韻地位
            None: {'鍾': '江'},
            '開': dict(zip(
                '支祭仙宵庚麻清鹽',
                '佳皆山肴庚麻庚咸'
            )),
            '合': dict(zip(
                '祭仙宵庚麻清鹽',
                '夬刪肴庚麻庚咸'
            )),
        }

        # TODO: 銳音移入常量後移除
        銳音 = '端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日以'

        # 首先生成等價但更優的音韻地位

        if 母 in 類隔[等]:
            母 = 類隔[等][母]
            合法性 = min(合法性, 合法性等級.無效)

        if 母到組(母) == '幫' and 韻 in 開合分韻:
            韻 = 開合分韻[韻]
            合法性 = min(合法性, 合法性等級.強非法)
        elif 母到組(母) != '幫' and 韻 == '凡':
            韻 = '嚴'
            呼 = '開'
            合法性 = min(合法性, 合法性等級.強非法)

        if 母 in 銳音 and 等 == '三' and 韻 in 銳音分韻:
            韻 = 銳音分韻[韻]
            合法性 = min(合法性, 合法性等級.強非法)

        if 母到組(母) == '莊':
            if 韻 in 莊三化二韻[呼] and 等 == '三':
                if 韻 in '鍾宵麻清':
                    # 此四韻無字，視爲非法
                    合法性 = min(合法性, 合法性等級.強非法)
                elif 韻 == '鹽':
                    # 鹽韻字少
                    合法性 = min(合法性, 合法性等級.弱合法)
                韻 = 莊三化二韻[呼][韻]
                等 = '二'
            elif 韻 == '佳' and 呼 == '合':
                韻 = '支'
                等 = '三'
                合法性 = min(合法性, 合法性等級.強非法)
            # 真臻之分也在此處理
            elif 韻 == '真' and 呼 == '開':
                韻 = '臻'
                合法性 = min(合法性, 合法性等級.弱非法)
            # 臻韻合口已被 驗證() 攔截，無需處理
        else:
            if 韻 == '臻':
                # 莊組以外聲母不能拼臻韻，屬於無效組合。這裡以真B韻作爲更優音韻地位
                韻 = '真'
                if 母 in 常量.重紐母:
                    重紐 = 'B'
                合法性 = min(合法性, 合法性等級.無效)

        # 庚三清之分
        if 韻 == '清' and (重紐 == 'B' or 母 == '云'):
            韻 = '庚'
            重紐 = None
            合法性 = min(合法性, 合法性等級.無效)
        elif 韻 == '庚' and 等 == '三' and 母 in 銳音 and 母到組(母) != '莊':
            韻 = '清'
            合法性 = min(合法性, 合法性等級.無效)

        更優音韻地位 = 音韻地位(母, 呼, 等, 重紐, 韻, 聲)

        # 接下來對更優音韻地位適用音位配列規則，檢驗其合法性
        for 音位配列規則 in 音位配列規則表:
            # TODO: 音韻表達式增加陰聲韻、銳鈍音之後移除以下部分
            音位配列規則 = list(音位配列規則)
            for i in (1, 2):
                if not 音位配列規則[i]:
                    continue
                音位配列規則[i] = 音位配列規則[i].replace(
                    '陰聲韻', '支脂之微魚虞模齊祭泰佳皆夬灰咍廢蕭宵肴豪歌麻尤侯幽韻').replace(
                    '次入韻', '祭泰夬廢韻').replace(
                    '鈍音', '幫滂並明見溪羣疑影曉匣云母').replace(
                    '銳音', '端透定泥來知徹澄孃精清從心邪莊初崇生俟章昌常書船日以母')
            # TODO: 音韻表達式增加陰聲韻、銳鈍音之後移除以上部分

            if 更優音韻地位.屬於(音位配列規則[1]) and not (音位配列規則[2] and 更優音韻地位.屬於(音位配列規則[2])):
                合法性 = min(合法性, 音位配列規則[0])
                break
        if 更優音韻地位 == self:
            更優音韻地位 = None
        return 合法性等級.到字符串(合法性), 更優音韻地位

    def __repr__(self) -> str:
        return '<音韻地位 ' + self.描述 + '>'

    def __eq__(self, that) -> bool:
        if not isinstance(that, 音韻地位):
            return False
        return self.最簡描述 == that.最簡描述

    def __hash__(self) -> int:
        return hash(self.最簡描述)
