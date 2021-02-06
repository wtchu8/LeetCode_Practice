#!/usr/bin/env python3

# Title: Sudoku Solver
# Link: https://leetcode.com/problems/sudoku-solver/
# Description: Write a program to solve a Sudoku puzzle by filling the empty cells.

# Results: In Progress

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Calculate possible values for each cell
            # go through all the rows and apply the row condition to the possible values
            # go through all the columns and apply the column condition to the possible values
            # go through each square and apply the square condition to the possible values
        # Identify any cell with only one possible value
        # If there are any cells like this, fill it in & recompute the possible values
        # if not, choose a cell with 2 possible values and test both conditions
        
        self.show_board(board)
        print(board)
    
    def show_board(self, board: List[List[str]]) -> None:
        for row in range(9):
            for col in range(9):
                print("|",board[row][col], end='', sep='')
            print("|")
            print("-------------------")
