# # # class Shape():
# # #     def __init__(self, w, l):
# # #         self.width = w
# # #         self.len = l
# # #
# # #     def print_size(self):
# # #         print("""{} by {}
# # #         """.format(self.width, self.len))
# # #
# # # class Square(Shape):
# # #     def area(self):
# # #         return self.width * self.len
# # #
# # #     def print_size(self):
# # #         print("""I am {} by {}
# # #         """.format(self.width, self.len))
# # #
# # # a_square = Square(20, 20)
# # # a_square.print_size()
# #
# # class Rectangle():
# #     recs = []
# #
# #     def __init__(self, w, l):
# #         self.width = w
# #         self.len = l
# #         self.recs.append((self.width, self.len))
# #
# #     def print_size(self):
# #         print("""{} by {}
# #         """.format(self.width, self.len))
# #
# #
# # r1 = Rectangle(10, 24)
# # r2 = Rectangle(11, 33)
# # r3 = Rectangle(12, 22)
# #
# # print(Rectangle.recs)
#
# class Card:
#     suits = ['spades',
#              'hearts',
#              'diamonds',
#              'clubs']
#     values = [None, None, '2', '3',
#               '4', '5', '6', '7',
#               '8', '9', '10',
#               'Jack', 'Queen',
#               'King', 'Ace',
#               ]
#
#     def __init__(self, v, s):
#         """suit + value are ints"""
#         self.value = v
#         self.suit = s
#
#     def __lt__(self, c2):
#         if self.value < c2.value:
#             return True
#         if self.value == c2.value:
#             if self.suit < c2.suite:
#                 return  True
#             else:
#                 return False
#         return False
#
#     def __gt__(self, c2):
#         if self.value > c2.value:
#             return True
#         if self.value == c2.value:
#             if self.suit > c2.suit:
#                 return True
#             else:
#                 return False
#         return False
#
#     def __repr__(self):
#         v = self.values[self.value] +\
#             'of' + \
#             self.suits[self.suit]
#         return v
#
#
# from random import shuffle
#
# class Deck:
#     def __init__(self):
#         self.cards = []
#         for i in range(2, 15):
#             for j in range(4):
#                 self.cards\
#                 .append(Card(i, j))
#         shuffle(self.cards)
#
#     def rm_card(self):
#         if len(self.cards) == 0:
#             return
#         return self.cards.pop()
#
# class Player:
#     def __init__(self, name):
#         self.wins = 0
#         self.card = None
#         self.name = name
#
# class Game:
#     def __init__(self):
#         name1 = input('p1 name')
#         name2 = input('p2 name')
#         self.deck = Deck()
#         self.p1 = Player(name1)
#         self.p2 = Player(name2)
#
#     def wins(self, winner):
#         w = '{} wins this round'
#         w = w.format(winner)
#         print(w)
#
#     def draw(self, p1n, p1c, p2n, p2c):
#         d = '{} drew {} {} drew'
#         d = d.format(p1n, p1c, p2n, p2c)
#         print(d)
#
#     def play_game(self):
#         cards = self.deck.cards
#         print('beginning War')
#         while len(cards) >= 2:
#             m = 'q to quit. Any ' +\
#                 'key to play'
#             response = input(m)
#             if response =='q':
#                 break

import re

line = '_one_two_three_'
found = re.findall('_.*?_', line)

for match in found:
    print(match)