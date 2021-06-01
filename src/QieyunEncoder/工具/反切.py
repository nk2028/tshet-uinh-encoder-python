# -*- coding: utf-8 -*-

'''
根據反切規律自動完成反切過程。
'''

from typing import List
from ..常量 import 常量
from ..音韻地位 import 音韻地位
from .._拓展音韻屬性 import 母到標準等


def _jointer(xs: List[str]):
    '''
    將多個字串以頓號和「或」字連接。

    ```python
    >>> _jointer(['A'])
    'A'
    >>> _jointer(['A', 'B'])
    'A或B'
    >>> _jointer(['A', 'B', 'C', 'D'])
    'A、B、C或D'
    ```
    '''
    return ''.join(x + '、' for x in xs[:-2]) + '或'.join(xs[-2:])


def 反切(上字音韻地位: 音韻地位, 下字音韻地位: 音韻地位, 顯示步驟=False, 類隔切=False):
    '''
    根據反切規律自動完成反切過程。

    當「顯示步驟」爲 `False` 時，回傳所有被切字音韻地位的列表。

    當「顯示步驟」爲 `True` 時，回傳 `dict`，包含「被切字音韻地位們」與「步驟」兩個字段。
    '''
    if 類隔切:
        raise NotImplementedError

    步驟 = []

    母 = 上字音韻地位.母
    步驟.append(f'反切上字爲{母}母，故被切字爲{母}母')

    韻 = 下字音韻地位.韻
    步驟.append(f'反切下字爲{韻}韻，故被切字爲{韻}韻')

    聲 = 下字音韻地位.聲
    步驟.append(f'反切下字爲{聲}聲，故被切字爲{聲}聲')

    # 確定呼

    if 母 in '幫滂並明':
        呼 = None
        # 步驟.append(f'{母}母屬於脣音，脣音字不分開合，故無需確定開合')
    elif 韻 in 常量.開合中立的韻:
        呼 = None
        # 步驟.append(f'{韻}韻是開合中立的韻，故無需確定開合')
    elif 韻 in 常量.必爲開口的韻:
        呼 = '開'
        步驟.append(f'{韻}韻必爲開口')
    elif 韻 in 常量.必爲合口的韻:
        呼 = '合'
        步驟.append(f'{韻}韻必爲合口')

    elif 上字音韻地位.呼 == '開' and 下字音韻地位.呼 == '開':
        呼 = '開'
        步驟.append(f'反切上下字均爲開口，故被切字爲開口')
    elif 下字音韻地位.呼 == '合':
        呼 = '合'
        步驟.append(f'反切下字爲合口，故被切字爲合口')
    elif 上字音韻地位.呼 == '合' and 下字音韻地位.組 == '幫':
        呼 = '合'
        步驟.append(f'反切上字爲合口，下字爲幫組，故被切字爲合口')
    else:
        呼 = '開合'
        步驟.append(f'無法確定開合，被切字可能爲開口或合口')

    # 確定等

    if 韻 in 常量.一等韻:
        等 = '一'
        步驟.append(f'{韻}韻必爲一等')
    elif 韻 in 常量.二等韻:
        等 = '二'
        步驟.append(f'{韻}韻必爲二等')
    elif 韻 in 常量.三等韻:
        等 = '三'
        步驟.append(f'{韻}韻必爲三等')
    elif 韻 in 常量.四等韻:
        等 = '四'
        步驟.append(f'{韻}韻必爲四等')

    elif 下字音韻地位.等 == '三':
        等 = '三'
        步驟.append(f'反切下字爲三等，故被切字爲三等')
    elif 上字音韻地位.等 != '三' and 下字音韻地位.等 != '三':
        if 韻 in 常量.一三等韻:
            等 = '一'
            步驟.append(f'{韻}韻必爲一等或三等')
            步驟.append(f'反切上下字均爲非三等，故被切字爲非三等，即被切字爲一等')
        elif 韻 in 常量.二三等韻:
            等 = '二'
            步驟.append(f'{韻}韻必爲二等或三等')
            步驟.append(f'反切上下字均爲非三等，故被切字爲非三等，即被切字爲二等')
        else:
            raise Exception('Unexpected 韻:' + 韻)
    else:
        if 韻 in 常量.一三等韻:
            等 = '一三'
            步驟.append(f'{韻}韻可能爲一等或三等')
        elif 韻 in 常量.二三等韻:
            等 = '二三'
            步驟.append(f'{韻}韻可能爲二等或三等')
        else:
            raise Exception('Unexpected 韻:' + 韻)

    # 確定重紐

    if 韻 not in 常量.重紐韻:
        重紐 = None
        # 步驟.append(f'{韻}韻無需確定重紐')
    elif 母 not in 常量.重紐母:
        重紐 = None
        # 步驟.append(f'{母}韻無需確定重紐')

    elif 上字音韻地位.重紐 is not None:
        重紐 = 上字音韻地位.重紐
        步驟.append(f'反切上字爲重紐{重紐}類，故被切字爲重紐{重紐}類')
    elif 下字音韻地位.屬於('重紐A類 或 以母 或 精組'):
        重紐 = 'A'
        步驟.append('反切下字爲重紐A類、以母或精組，被切字爲重紐A類')
    elif 下字音韻地位.屬於('重紐B類 云母'):
        重紐 = 'B'
        步驟.append('反切下字爲重紐B類或云母，被切字爲重紐B類')
    else:
        重紐 = 'AB'
        步驟.append('不能確定重紐，被切字可能爲重紐A類或重紐B類')

    # 母對等的約束

    標準等 = 母到標準等[母]
    if any(等1 not in 標準等 for 等1 in 等):
        等 = ''.join(等1 for 等1 in 等 if 等1 in 標準等)
        步驟.append(f'{母}母只能爲{標準等}等')

    # 組合被切字所有可能等音韻地位

    被切字音韻地位們 = [
        音韻地位(母, 呼1, 等1, 重紐1, 韻, 聲)
        for 呼1 in (呼 if 呼 == '開合' else (呼,))
        for 等1 in (等 if 等 in ('一三', '二三') else 等)
        for 重紐1 in (重紐 if 重紐 == 'AB' else (重紐,))
    ]

    if not 被切字音韻地位們:
        步驟.append('故爲不合法音節')
    else:
        步驟.append('故被切字的音韻地位爲' + _jointer([
            被切字音韻地位.描述
            for 被切字音韻地位 in 被切字音韻地位們
        ]))

    if not 顯示步驟:
        return 被切字音韻地位們
    else:
        return {
            '被切字音韻地位們': 被切字音韻地位們,
            '步驟': 步驟
        }
