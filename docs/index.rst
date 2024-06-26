.. Tshet-uinh Encoder Python  documentation master file, created by
   sphinx-quickstart on Wed Apr 17 04:51:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tshet-uinh Encoder Python 說明文件
==================================

.. toctree::
   :maxdepth: 1

   常量
   轉換
   音韻地位
   韻鏡位置
   工具


音韻屬性
--------

母、音、組、清濁
^^^^^^^^^^^^^^^^

母採用三十八聲類的分類方法。

.. raw:: html

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

    .. raw:: html

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

    區別如下:

    - 幫滂並明在三等輕脣韻前分化爲非敷奉微
    - 云以母合流爲喻母
    - 莊章組合流爲照組

呼
^^

取值：開、合、``None``。其中 ``None`` 表示開合中立。

脣音的開合必爲 ``None``。

韻與開合的關係如下:

- 開合兼備的韻：支脂微齊祭泰佳皆夬廢眞元寒刪山仙先歌麻陽唐庚耕清青蒸登
- 必爲開口的韻：咍痕欣嚴之魚臻蕭宵肴豪侯侵覃談鹽添咸銜
- 必爲合口的韻：灰魂文凡
- 開合中立的韻：東冬鍾江虞模尤幽

.. hint::

    不要與韻鏡的開合混淆。

    以《韻鏡》爲例，開合有三種取值：開、合、開合。

    - 在《韻鏡》中，對脣音沒有特殊處理。而在此處，脣音的開合必爲 ``None``
    - 《韻鏡》所標「開合」與此處開合中立的韻的劃分並不完全相同
    - 《韻鏡》存在誤標開合的情況，如第四轉「內轉第四開合」當爲「內轉第四開」

等
^^

取值：一、二、三、四。

韻與等的關係如下:

- 一等韻：冬模泰咍灰痕魂寒豪唐登侯覃談
- 二等韻：江佳皆夬刪山肴耕咸銜
- 三等韻：鍾支脂之微魚虞祭廢眞臻欣元文仙宵陽清蒸尤幽侵鹽嚴凡
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

重紐
^^^^

取值：``None``、重紐A類、重紐B類。

- 重紐母：幫滂並明見溪羣疑影曉
- 重紐韻：支脂祭眞仙宵清侵鹽

當聲紐不爲重紐母，或韻不爲重紐韻時，重紐必須爲 ``None``。

清韻重紐母取重紐A類。

韻、攝
^^^^^^

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

    使用殷韻的名稱，不使用欣韻；使用真韻的寫法，不使用眞韻。但構造函式及 ``from描述`` 方法具備容錯功能，會執行自動轉換。

聲
^^

取值：平、上、去、入；仄、舒。

其中，仄表示上去入聲，舒表示平上去聲。
