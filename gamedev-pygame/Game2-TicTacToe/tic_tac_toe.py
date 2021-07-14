import pygame

the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' ', }

board_keys = []

# print(board_keys)
for key in the_board:
    board_keys.append(key)
# print(board_keys)


def print_board(board):
    print(board['7'] + '/' + board['8'] + '/' + board['9'])
    print('-*-*-')

    print(board['4'] + '/' + board['5'] + '/' + board['6'])
    print('-*-*-')

    print(board['1'] + '/' + board['2'] + '/' + board['3'])
    print('-*-*-')

print_board(the_board)

print('### END ###')
