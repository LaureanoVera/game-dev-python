import os
import sys
import cfg
import random
import pygame

def is_game_over(board, size):
  assert is_instance(size, int)
  num_cells = size * size
  for i in range(num_cells - 1):
    if board[i] != i: False
  return True

def move_r(board, blank_cell_idx, num_cols):
  if blank_cell_idx % num_cols == 0: return blank_cell_idx
  board[blank_cell_idx-1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-1]
  return blank_cell_idx-1

def move_l(board, blank_cell_idx, num_cols):
  if (blank_cell_idx+1) % num_cols == 0: return blank_cell_idx
  board[blank_cell_idx+1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
  return blank_cell_idx+1

def move_d(board, blank_cell_idx, num_cols):
  if blank_cell_idx < num_cols: return blank_cell_idx
  board[blank_cell_idx-num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-num_cols]
  return blank_cell_idx-num_cols

def move_t(board, blank_cell_idx, num_rows, num_cols):
  if blank_cell_idx >= (num_rows-1) * num_cols: return blank_cell_idx
  board[blank_cell_idx+num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+num_cols]
  return blank_cell_idx+num_cols

def create_board(num_rows, num_cols, num_cells):
  board=[]

  for i in range(num_cells):
    board.append(i)

  blank_cell_idx = num_cells - 1
  board[blank_cell_idx] = -1

  for i in range(cfg.RANDNUM):
    direction = random.randint(0, 3)

    if direction == 0:
      blank_cell_idx = move_l(board, blank_cell_idx, num_cols)
    elif direction == 1:
      blank_cell_idx = move_r(board, blank_cell_idx, num_cols)
    elif direction == 2:
      blank_cell_idx = move_t(board, blank_cell_idx, num_rows, num_cols)
    elif direction == 3:
      blank_cell_idx = move_d(board, blank_cell_idx, num_cols)
  
  return board, blank_cell_idx


if __name__ == '__main__':
    main()
