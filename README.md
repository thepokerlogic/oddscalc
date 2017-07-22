# oddscalc
本项目用以解释手牌胜率计算的原理。

详细信息请参阅：[http://thepokerlogic.com/post/oddscalc.html][1]

PokerLogic的线上胜率计算器：[http://thepokerlogic.com/post/oddscalc.html][2]

## 扑克牌的定义
Rank 大小，从2到A
Suit 花色，spade，heart，diamond，club，取首字缩写，AS代表黑桃A，以此类推。
## Ranking 
* rank_kickers(), 用小数位上2的倍数来判断踢脚的大小_
* rank_hand_Int(), 用字符串匹配的方式，依次判断手牌+公共牌组成的最大牌型牌力，最后加入踢脚值
## 获得胜率
循环出所有剩余牌型，分别记录获胜的次数，并得出总数

[1]:	http://thepokerlogic.com/post/oddscalc.html
[2]:	http://thepokerlogic.com/post/oddscalc.html