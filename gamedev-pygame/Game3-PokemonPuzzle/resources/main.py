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
  board[blank_cell_id+1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
  return blank_cell_idx+1

if __name__ == '__main__':
    main()
