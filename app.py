# -*- coding: UTF-8 -*-
class Deck():
    def __init__(self):
        deck = []
        deck.append('AS')
        deck.append('KS')
        deck.append('QS')
        deck.append('JS')
        deck.append('TS')
        deck.append('9S')
        deck.append('8S')
        deck.append('7S')
        deck.append('6S')
        deck.append('5S')
        deck.append('4S')
        deck.append('3S')
        deck.append('2S')
        deck.append('AH')
        deck.append('KH')
        deck.append('QH')
        deck.append('JH')
        deck.append('TH')
        deck.append('9H')
        deck.append('8H')
        deck.append('7H')
        deck.append('6H')
        deck.append('5H')
        deck.append('4H')
        deck.append('3H')
        deck.append('2H')
        deck.append('AD')
        deck.append('KD')
        deck.append('QD')
        deck.append('JD')
        deck.append('TD')
        deck.append('9D')
        deck.append('8D')
        deck.append('7D')
        deck.append('6D')
        deck.append('5D')
        deck.append('4D')
        deck.append('3D')
        deck.append('2D')
        deck.append('AC')
        deck.append('KC')
        deck.append('QC')
        deck.append('JC')
        deck.append('TC')
        deck.append('9C')
        deck.append('8C')
        deck.append('7C')
        deck.append('6C')
        deck.append('5C')
        deck.append('4C')
        deck.append('3C')
        deck.append('2C')
        self.deck = deck

class SevenCards():
    def __init__(self,cards,rank,card_type):
        self.cards = cards
        self.rank = rank
        self.card_type = card_type

def board_all(deck, cards=[], dead=[]):

    # 移除已知牌
    for card in cards:
        deck.remove(card)

    # 移除死牌
    for card in dead:
        deck.remove(card)

    boards = []
    board = [''] * (5 - len(cards))
    remaining_cards_count = 5 - len(cards)

    def deck_list(deck_l=[], index=0):

        for i in range(len(deck_l)):
            board[index] = deck_l[i]
            deck_left = deck_l[i + 1:]
            if index < remaining_cards_count - 1:
                deck_list(deck_left, index + 1)
            else:
                boards.append(board[0:])

    deck_list(deck, 0)
    return boards

def _sort(pokers):
    def tmp(poker):
        ranks = 'AKQJT98765432'
        return (ranks.index(poker[0]))
    return sorted(pokers, key=tmp)

def rank_kickers(ranks = '', no_of_cards = 0):

    kicker_rank = 0.0000
    for i in range(no_of_cards):
        rank = ranks[i]
        if rank == 'A':
            kicker_rank += 0.2048
        elif rank == 'K':
            kicker_rank += 0.1024
        elif rank == 'Q':
            kicker_rank += 0.0512
        elif rank == 'J':
            kicker_rank += 0.0256
        elif rank == 'T':
            kicker_rank += 0.0128
        elif rank == '9':
            kicker_rank += 0.0064
        elif rank == '8':
            kicker_rank += 0.0032
        elif rank == '7':
            kicker_rank += 0.0016
        elif rank == '6':
            kicker_rank += 0.0008
        elif rank == '5':
            kicker_rank += 0.0004
        elif rank == '4':
            kicker_rank += 0.0002
        elif rank == '3':
            kicker_rank += 0.0001
        elif rank == '2':
            kicker_rank += 0.0000
    return  kicker_rank

def rank_hand_Int(cards):

    rank = 0.0000
    card_type = ''

    hand_ranks = ['', '', '', '', '', '', '']
    hand_suits = ['', '', '', '', '', '', '']

    for i in range(len(cards)):
        hand_ranks[i] = cards[i][0]
        hand_suits[i] = cards[i][1]
    hand_ranks = _sort(hand_ranks)
    hand_suits.sort()
    ranks = ''.join(hand_ranks)

    suits = ''.join(hand_suits)

    # Four of a kind
    if rank == 0:

        if ranks.find('AAAA') > -1:
            rank = 292 + rank_kickers(ranks.replace('AAAA', ''), 1)
        if ranks.find('KKKK') > -1:
            rank = 291 + rank_kickers(ranks.replace('KKKK', ''), 1)
        if ranks.find('QQQQ') > -1:
            rank = 290 + rank_kickers(ranks.replace('QQQQ', ''), 1)
        if ranks.find('JJJJ') > -1:
            rank = 289 + rank_kickers(ranks.replace('JJJJ', ''), 1)
        if ranks.find('TTTT') > -1:
            rank = 288 + rank_kickers(ranks.replace('TTTT', ''), 1)
        if ranks.find('9999') > -1:
            rank = 287 + rank_kickers(ranks.replace('9999', ''), 1)
        if ranks.find('8888') > -1:
            rank = 286 + rank_kickers(ranks.replace('8888', ''), 1)
        if ranks.find('7777') > -1:
            rank = 285 + rank_kickers(ranks.replace('7777', ''), 1)
        if ranks.find('6666') > -1:
            rank = 284 + rank_kickers(ranks.replace('6666', ''), 1)
        if ranks.find('5555') > -1:
            rank = 283 + rank_kickers(ranks.replace('5555', ''), 1)
        if ranks.find('4444') > -1:
            rank = 282 + rank_kickers(ranks.replace('4444', ''), 1)
        if ranks.find('3333') > -1:
            rank = 281 + rank_kickers(ranks.replace('3333', ''), 1)
        if ranks.find('2222') > -1:
            rank = 280 + rank_kickers(ranks.replace('2222', ''), 1)
        if rank != 0:
            card_type = 'Four of a kind'

    # Full House
    if rank == 0:

        if ranks.find('AAA') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 279
        if ranks.find('AAA') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 278
        if ranks.find('AAA') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 277
        if ranks.find('AAA') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 276
        if ranks.find('AAA') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 275
        if ranks.find('AAA') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 274
        if ranks.find('AAA') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 273
        if ranks.find('AAA') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 272
        if ranks.find('AAA') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 271
        if ranks.find('AAA') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 270
        if ranks.find('AAA') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 269
        if ranks.find('AAA') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 268
        if ranks.find('KKK') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 267
        if ranks.find('KKK') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 266
        if ranks.find('KKK') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 265
        if ranks.find('KKK') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 264
        if ranks.find('KKK') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 263
        if ranks.find('KKK') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 262
        if ranks.find('KKK') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 261
        if ranks.find('KKK') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 260
        if ranks.find('KKK') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 259
        if ranks.find('KKK') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 258
        if ranks.find('KKK') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 257
        if ranks.find('KKK') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 256
        if ranks.find('QQQ') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 255
        if ranks.find('QQQ') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 254
        if ranks.find('QQQ') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 253
        if ranks.find('QQQ') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 252
        if ranks.find('QQQ') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 251
        if ranks.find('QQQ') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 250
        if ranks.find('QQQ') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 249
        if ranks.find('QQQ') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 248
        if ranks.find('QQQ') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 247
        if ranks.find('QQQ') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 246
        if ranks.find('QQQ') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 245
        if ranks.find('QQQ') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 244
        if ranks.find('JJJ') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 243
        if ranks.find('JJJ') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 242
        if ranks.find('JJJ') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 241
        if ranks.find('JJJ') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 240
        if ranks.find('JJJ') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 239
        if ranks.find('JJJ') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 238
        if ranks.find('JJJ') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 237
        if ranks.find('JJJ') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 236
        if ranks.find('JJJ') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 235
        if ranks.find('JJJ') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 234
        if ranks.find('JJJ') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 233
        if ranks.find('JJJ') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 232
        if ranks.find('TTT') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 231
        if ranks.find('TTT') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 230
        if ranks.find('TTT') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 229
        if ranks.find('TTT') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 228
        if ranks.find('TTT') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 227
        if ranks.find('TTT') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 226
        if ranks.find('TTT') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 225
        if ranks.find('TTT') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 224
        if ranks.find('TTT') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 223
        if ranks.find('TTT') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 222
        if ranks.find('TTT') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 221
        if ranks.find('TTT') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 220
        if ranks.find('999') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 219
        if ranks.find('999') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 218
        if ranks.find('999') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 217
        if ranks.find('999') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 216
        if ranks.find('999') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 215
        if ranks.find('999') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 214
        if ranks.find('999') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 213
        if ranks.find('999') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 212
        if ranks.find('999') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 211
        if ranks.find('999') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 210
        if ranks.find('999') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 209
        if ranks.find('999') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 208
        if ranks.find('888') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 207
        if ranks.find('888') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 206
        if ranks.find('888') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 205
        if ranks.find('888') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 204
        if ranks.find('888') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 203
        if ranks.find('888') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 202
        if ranks.find('888') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 201
        if ranks.find('888') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 200
        if ranks.find('888') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 199
        if ranks.find('888') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 198
        if ranks.find('888') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 197
        if ranks.find('888') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 196
        if ranks.find('777') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 195
        if ranks.find('777') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 194
        if ranks.find('777') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 193
        if ranks.find('777') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 192
        if ranks.find('777') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 191
        if ranks.find('777') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 190
        if ranks.find('777') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 189
        if ranks.find('777') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 188
        if ranks.find('777') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 187
        if ranks.find('777') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 186
        if ranks.find('777') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 185
        if ranks.find('777') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 184
        if ranks.find('666') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 183
        if ranks.find('666') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 182
        if ranks.find('666') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 181
        if ranks.find('666') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 180
        if ranks.find('666') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 179
        if ranks.find('666') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 178
        if ranks.find('666') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 177
        if ranks.find('666') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 176
        if ranks.find('666') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 175
        if ranks.find('666') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 174
        if ranks.find('666') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 173
        if ranks.find('666') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 172
        if ranks.find('555') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 171
        if ranks.find('555') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 170
        if ranks.find('555') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 169
        if ranks.find('555') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 168
        if ranks.find('555') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 167
        if ranks.find('555') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 166
        if ranks.find('555') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 165
        if ranks.find('555') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 164
        if ranks.find('555') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 163
        if ranks.find('555') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 162
        if ranks.find('555') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 161
        if ranks.find('555') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 160
        if ranks.find('444') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 159
        if ranks.find('444') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 158
        if ranks.find('444') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 157
        if ranks.find('444') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 156
        if ranks.find('444') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 155
        if ranks.find('444') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 154
        if ranks.find('444') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 153
        if ranks.find('444') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 152
        if ranks.find('444') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 151
        if ranks.find('444') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 150
        if ranks.find('444') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 149
        if ranks.find('444') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 148
        if ranks.find('333') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 147
        if ranks.find('333') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 146
        if ranks.find('333') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 145
        if ranks.find('333') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 144
        if ranks.find('333') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 143
        if ranks.find('333') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 142
        if ranks.find('333') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 141
        if ranks.find('333') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 140
        if ranks.find('333') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 139
        if ranks.find('333') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 138
        if ranks.find('333') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 137
        if ranks.find('333') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 136
        if ranks.find('222') > -1 and ranks.find('AA') > -1 and rank == 0:
            rank = 135
        if ranks.find('222') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 134
        if ranks.find('222') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 133
        if ranks.find('222') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 132
        if ranks.find('222') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 131
        if ranks.find('222') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 130
        if ranks.find('222') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 129
        if ranks.find('222') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 128
        if ranks.find('222') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 127
        if ranks.find('222') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 126
        if ranks.find('222') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 125
        if ranks.find('222') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 124
        if rank != 0:
            card_type = 'Full House'
    # Flush
    if rank == 0:

        flush_t = ''
        if suits.find('CCCCC') > -1:
            rank = 123
            flush_t = 'C'
        if suits.find('DDDDD') > -1:
            rank = 123
            flush_t = 'D'
        if suits.find('HHHHH') > -1:
            rank = 123
            flush_t = 'H'
        if suits.find('SSSSS') > -1:
            rank = 123
            flush_t = 'S'

        if rank == 123:
            ranks_flush = []
            for card in cards:
                if card.find(flush_t) > -1:
                    ranks_flush.append(card[0])
            ranks_flush = _sort(ranks_flush)
            ranks = ''.join(ranks_flush)

        # Straight flush
        if ranks.find('AKQJT') > -1 and rank == 123:
            rank = 302
        if ranks.find('KQJT9') > -1 and rank == 123:
            rank = 301
        if ranks.find('QJT98') > -1 and rank == 123:
            rank = 300
        if ranks.find('JT987') > -1 and rank == 123:
            rank = 299
        if ranks.find('T9876') > -1 and rank == 123:
            rank = 298
        if ranks.find('98765') > -1 and rank == 123:
            rank = 297
        if ranks.find('87654') > -1 and rank == 123:
            rank = 296
        if ranks.find('76543') > -1 and rank == 123:
            rank = 295
        if ranks.find('65432') > -1 and rank == 123:
            rank = 294
        if ranks.find('A') > -1 and ranks.find('5432') > -1 and rank == 123:
            rank = 293
        if rank == 123:
            rank += rank_kickers(''.join(ranks_flush), 5)
            card_type = 'Flush'
        else:
            card_type = 'Straight Flush'

    # Straight
    if rank == 0:
        if ranks.find('AKQJT') > -1 and rank == 0:
            rank = 122
        if ranks.find('KQJT9') > -1 and rank == 0:
            rank = 121
        if ranks.find('QJT98') > -1 and rank == 0:
            rank = 120
        if ranks.find('JT987') > -1 and rank == 0:
            rank = 119
        if ranks.find('T9876') > -1 and rank == 0:
            rank = 118
        if ranks.find('98765') > -1 and rank == 0:
            rank = 117
        if ranks.find('87654') > -1 and rank == 0:
            rank = 116
        if ranks.find('76543') > -1 and rank == 0:
            rank = 115
        if ranks.find('65432') > -1 and rank == 0:
            rank = 114
        if ranks.find('A') > -1 and ranks.find('5432') > -1 and rank == 0:
            rank = 113
        if rank != 0:
            card_type = 'Straight'

    # Three of a kind
    if rank == 0:

        if ranks.find('AAA') > -1 and rank == 0:
            rank = 112 + rank_kickers(ranks.replace('AAA', ''), 2)
        if ranks.find('KKK') > -1 and rank == 0:
            rank = 111 + rank_kickers(ranks.replace('KKK', ''), 2)
        if ranks.find('QQQ') > -1 and rank == 0:
            rank = 110 + rank_kickers(ranks.replace('QQQ', ''), 2)
        if ranks.find('JJJ') > -1 and rank == 0:
            rank = 109 + rank_kickers(ranks.replace('JJJ', ''), 2)
        if ranks.find('TTT') > -1 and rank == 0:
            rank = 108 + rank_kickers(ranks.replace('TTT', ''), 2)
        if ranks.find('999') > -1 and rank == 0:
            rank = 107 + rank_kickers(ranks.replace('999', ''), 2)
        if ranks.find('888') > -1 and rank == 0:
            rank = 106 + rank_kickers(ranks.replace('888', ''), 2)
        if ranks.find('777') > -1 and rank == 0:
            rank = 105 + rank_kickers(ranks.replace('777', ''), 2)
        if ranks.find('666') > -1 and rank == 0:
            rank = 104 + rank_kickers(ranks.replace('666', ''), 2)
        if ranks.find('555') > -1 and rank == 0:
            rank = 103 + rank_kickers(ranks.replace('555', ''), 2)
        if ranks.find('444') > -1 and rank == 0:
            rank = 102 + rank_kickers(ranks.replace('444', ''), 2)
        if ranks.find('333') > -1 and rank == 0:
            rank = 101 + rank_kickers(ranks.replace('333', ''), 2)
        if ranks.find('222') > -1 and rank == 0:
            rank = 100 + rank_kickers(ranks.replace('222', ''), 2)
        if rank != 0:
            card_type = 'Three of a Kind'
    # Two pair
    if rank == 0:

        if ranks.find('AA') > -1 and ranks.find('KK') > -1 and rank == 0:
            rank = 99 + rank_kickers(ranks.replace('AA', '').replace('KK', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 98 + rank_kickers(ranks.replace('AA', '').replace('QQ', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 97 + rank_kickers(ranks.replace('AA', '').replace('JJ', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 96 + rank_kickers(ranks.replace('AA', '').replace('TT', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 95 + rank_kickers(ranks.replace('AA', '').replace('99', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 94 + rank_kickers(ranks.replace('AA', '').replace('88', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 93 + rank_kickers(ranks.replace('AA', '').replace('77', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 92 + rank_kickers(ranks.replace('AA', '').replace('66', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 91 + rank_kickers(ranks.replace('AA', '').replace('55', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 90 + rank_kickers(ranks.replace('AA', '').replace('44', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 89 + rank_kickers(ranks.replace('AA', '').replace('33', ''), 1)
        if ranks.find('AA') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 88 + rank_kickers(ranks.replace('AA', '').replace('22', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('QQ') > -1 and rank == 0:
            rank = 87 + rank_kickers(ranks.replace('KK', '').replace('QQ', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 86 + rank_kickers(ranks.replace('KK', '').replace('JJ', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 85 + rank_kickers(ranks.replace('KK', '').replace('TT', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 84 + rank_kickers(ranks.replace('KK', '').replace('99', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 83 + rank_kickers(ranks.replace('KK', '').replace('88', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 82 + rank_kickers(ranks.replace('KK', '').replace('77', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 81 + rank_kickers(ranks.replace('KK', '').replace('66', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 80 + rank_kickers(ranks.replace('KK', '').replace('55', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 79 + rank_kickers(ranks.replace('KK', '').replace('44', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 78 + rank_kickers(ranks.replace('KK', '').replace('33', ''), 1)
        if ranks.find('KK') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 77 + rank_kickers(ranks.replace('KK', '').replace('22', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('JJ') > -1 and rank == 0:
            rank = 76 + rank_kickers(ranks.replace('QQ', '').replace('JJ', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 75 + rank_kickers(ranks.replace('QQ', '').replace('TT', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 74 + rank_kickers(ranks.replace('QQ', '').replace('99', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 73 + rank_kickers(ranks.replace('QQ', '').replace('88', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 72 + rank_kickers(ranks.replace('QQ', '').replace('77', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 71 + rank_kickers(ranks.replace('QQ', '').replace('66', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 70 + rank_kickers(ranks.replace('QQ', '').replace('55', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 69 + rank_kickers(ranks.replace('QQ', '').replace('44', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 68 + rank_kickers(ranks.replace('QQ', '').replace('33', ''), 1)
        if ranks.find('QQ') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 67 + rank_kickers(ranks.replace('QQ', '').replace('22', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('TT') > -1 and rank == 0:
            rank = 66 + rank_kickers(ranks.replace('JJ', '').replace('TT', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 65 + rank_kickers(ranks.replace('JJ', '').replace('99', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 64 + rank_kickers(ranks.replace('JJ', '').replace('88', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 63 + rank_kickers(ranks.replace('JJ', '').replace('77', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 62 + rank_kickers(ranks.replace('JJ', '').replace('66', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 61 + rank_kickers(ranks.replace('JJ', '').replace('55', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 60 + rank_kickers(ranks.replace('JJ', '').replace('44', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 59 + rank_kickers(ranks.replace('JJ', '').replace('33', ''), 1)
        if ranks.find('JJ') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 58 + rank_kickers(ranks.replace('JJ', '').replace('22', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('99') > -1 and rank == 0:
            rank = 57 + rank_kickers(ranks.replace('TT', '').replace('99', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 56 + rank_kickers(ranks.replace('TT', '').replace('88', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 55 + rank_kickers(ranks.replace('TT', '').replace('77', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 54 + rank_kickers(ranks.replace('TT', '').replace('66', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 53 + rank_kickers(ranks.replace('TT', '').replace('55', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 52 + rank_kickers(ranks.replace('TT', '').replace('44', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 51 + rank_kickers(ranks.replace('TT', '').replace('33', ''), 1)
        if ranks.find('TT') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 50 + rank_kickers(ranks.replace('TT', '').replace('22', ''), 1)
        if ranks.find('99') > -1 and ranks.find('88') > -1 and rank == 0:
            rank = 49 + rank_kickers(ranks.replace('99', '').replace('88', ''), 1)
        if ranks.find('99') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 48 + rank_kickers(ranks.replace('99', '').replace('77', ''), 1)
        if ranks.find('99') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 47 + rank_kickers(ranks.replace('99', '').replace('66', ''), 1)
        if ranks.find('99') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 46 + rank_kickers(ranks.replace('99', '').replace('55', ''), 1)
        if ranks.find('99') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 45 + rank_kickers(ranks.replace('99', '').replace('44', ''), 1)
        if ranks.find('99') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 44 + rank_kickers(ranks.replace('99', '').replace('33', ''), 1)
        if ranks.find('99') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 43 + rank_kickers(ranks.replace('99', '').replace('22', ''), 1)
        if ranks.find('88') > -1 and ranks.find('77') > -1 and rank == 0:
            rank = 42 + rank_kickers(ranks.replace('88', '').replace('77', ''), 1)
        if ranks.find('88') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 41 + rank_kickers(ranks.replace('88', '').replace('66', ''), 1)
        if ranks.find('88') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 40 + rank_kickers(ranks.replace('88', '').replace('55', ''), 1)
        if ranks.find('88') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 39 + rank_kickers(ranks.replace('88', '').replace('44', ''), 1)
        if ranks.find('88') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 38 + rank_kickers(ranks.replace('88', '').replace('33', ''), 1)
        if ranks.find('88') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 37 + rank_kickers(ranks.replace('88', '').replace('22', ''), 1)
        if ranks.find('77') > -1 and ranks.find('66') > -1 and rank == 0:
            rank = 36 + rank_kickers(ranks.replace('77', '').replace('66', ''), 1)
        if ranks.find('77') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 35 + rank_kickers(ranks.replace('77', '').replace('55', ''), 1)
        if ranks.find('77') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 34 + rank_kickers(ranks.replace('77', '').replace('44', ''), 1)
        if ranks.find('77') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 33 + rank_kickers(ranks.replace('77', '').replace('33', ''), 1)
        if ranks.find('77') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 32 + rank_kickers(ranks.replace('77', '').replace('22', ''), 1)
        if ranks.find('66') > -1 and ranks.find('55') > -1 and rank == 0:
            rank = 31 + rank_kickers(ranks.replace('66', '').replace('55', ''), 1)
        if ranks.find('66') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 30 + rank_kickers(ranks.replace('66', '').replace('44', ''), 1)
        if ranks.find('66') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 29 + rank_kickers(ranks.replace('66', '').replace('33', ''), 1)
        if ranks.find('66') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 28 + rank_kickers(ranks.replace('66', '').replace('22', ''), 1)
        if ranks.find('55') > -1 and ranks.find('44') > -1 and rank == 0:
            rank = 27 + rank_kickers(ranks.replace('55', '').replace('44', ''), 1)
        if ranks.find('55') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 26 + rank_kickers(ranks.replace('55', '').replace('33', ''), 1)
        if ranks.find('55') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 25 + rank_kickers(ranks.replace('55', '').replace('22', ''), 1)
        if ranks.find('44') > -1 and ranks.find('33') > -1 and rank == 0:
            rank = 24 + rank_kickers(ranks.replace('44', '').replace('33', ''), 1)
        if ranks.find('44') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 23 + rank_kickers(ranks.replace('44', '').replace('22', ''), 1)
        if ranks.find('33') > -1 and ranks.find('22') > -1 and rank == 0:
            rank = 22 + rank_kickers(ranks.replace('33', '').replace('22', ''), 1)
        if rank != 0:
            card_type = 'Two Pair'
    # One Pair
    if rank == 0:

        if ranks.find('AA') > -1 and rank == 0:
            rank = 21 + rank_kickers(ranks.replace('AA', ''), 3)
        if ranks.find('KK') > -1 and rank == 0:
            rank = 20 + rank_kickers(ranks.replace('KK', ''), 3)
        if ranks.find('QQ') > -1 and rank == 0:
            rank = 19 + rank_kickers(ranks.replace('QQ', ''), 3)
        if ranks.find('JJ') > -1 and rank == 0:
            rank = 18 + rank_kickers(ranks.replace('JJ', ''), 3)
        if ranks.find('TT') > -1 and rank == 0:
            rank = 17 + rank_kickers(ranks.replace('TT', ''), 3)
        if ranks.find('99') > -1 and rank == 0:
            rank = 16 + rank_kickers(ranks.replace('99', ''), 3)
        if ranks.find('88') > -1 and rank == 0:
            rank = 15 + rank_kickers(ranks.replace('88', ''), 3)
        if ranks.find('77') > -1 and rank == 0:
            rank = 14 + rank_kickers(ranks.replace('77', ''), 3)
        if ranks.find('66') > -1 and rank == 0:
            rank = 13 + rank_kickers(ranks.replace('66', ''), 3)
        if ranks.find('55') > -1 and rank == 0:
            rank = 12 + rank_kickers(ranks.replace('55', ''), 3)
        if ranks.find('44') > -1 and rank == 0:
            rank = 11 + rank_kickers(ranks.replace('44', ''), 3)
        if ranks.find('33') > -1 and rank == 0:
            rank = 10 + rank_kickers(ranks.replace('33', ''), 3)
        if ranks.find('22') > -1 and rank == 0:
            rank = 9 + rank_kickers(ranks.replace('22', ''), 3)
        if rank != 0:
            card_type = 'Pair'
    # High Card
    if rank == 0:
        if ranks.find('A') > -1 and rank == 0:
            rank = 8 + rank_kickers(ranks.replace('A', ''), 4)
        if ranks.find('K') > -1 and rank == 0:
            rank = 7 + rank_kickers(ranks.replace('K', ''), 4)
        if ranks.find('Q') > -1 and rank == 0:
            rank = 6 + rank_kickers(ranks.replace('Q', ''), 4)
        if ranks.find('J') > -1 and rank == 0:
            rank = 5 + rank_kickers(ranks.replace('J', ''), 4)
        if ranks.find('T') > -1 and rank == 0:
            rank = 4 + rank_kickers(ranks.replace('T', ''), 4)
        if ranks.find('9') > -1 and rank == 0:
            rank = 3 + rank_kickers(ranks.replace('9', ''), 4)
        if ranks.find('8') > -1 and rank == 0:
            rank = 2 + rank_kickers(ranks.replace('8', ''), 4)
        if ranks.find('7') > -1 and rank == 0:
            rank = 1 + rank_kickers(ranks.replace('7', ''), 4)
        if rank != 0:
            card_type = 'High Card'
    seven_cards = SevenCards(cards=cards, rank=rank, card_type=card_type)
    return seven_cards

def win(hands_arr=[], board=[], dead=[]):

    deck = Deck().deck

    for hands in hands_arr:
        for hand in hands:
            deck.remove(hand)

    if len(board) < 5:
        deck_list = board_all(deck, board, dead)
        count = [0] * len(hands_arr)
        count_eq = 0
        for deck_hand in deck_list:
            rank_r = []
            for hands in hands_arr:
                hole_board_cards = deck_hand + hands + board
                seven_cards = rank_hand_Int(hole_board_cards)
                rank_r.append(seven_cards.rank)
            max_obj = max(rank_r)
            max_index_arr = [i for i, j in enumerate(rank_r) if j == max_obj]
            for index in max_index_arr:
                count[index] += 1
            if len(max_index_arr) > 1 and len(hands_arr) == 2:
                count_eq += 1
        print(count)
        print(count_eq)
    else:
        rank_r = []
        count = [0] * len(hands_arr)
        for hands in hands_arr:
            hole_board_cards = hands + board
            seven_cards = rank_hand_Int(hole_board_cards)
            rank_r.append(seven_cards.rank)

        max_obj = max(rank_r)
        max_index_arr = [i for i, j in enumerate(rank_r) if j == max_obj]
        for index in max_index_arr:
            count[index] += 1
        print(count)

win([['AC','AS'],['TC','TS']],['5C','4C','3C','2C','4S'])