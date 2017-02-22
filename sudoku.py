#Goal: solve the sudoku game 

import sys

class sudoku():

  def __init__(self, puzzle):

    self.puzzle = [int(v) for v in puzzle]





  def __repr__(self):

    return "".join(str(x) for x in self.puzzle) + "\n"


  def __str__(self):

    return "My great sudoku puzzle: " + str(self.puzzle)

  def verify_uniq(self, input_list):
    number_set = set()
    for i in input_list:
      if i<1 or i>9:
        return False
      number_set.add(i)
    if len(number_set) != 9:
      return False
    return True

  def verify_solution(self):    
   # verify each row.
    for i in range(9):
      number_set = set()
      for j in range(9):
        current_number = self.puzzle[i*9 + j]
        if current_number<1 or current_number>9:
          return False
        number_set.add(current_number)
      if len(number_set) != 9:
        return False
    # verify each column.
    for i in range(9):
      number_set = set()
      for j in range(9):
        current_number = self.puzzle[i + j*9]
        if current_number<1 or current_number>9:
          return False
        number_set.add(current_number)
      if len(number_set) != 9:
        return False
    # verify each box.
    for i in range(81): 
      if not self.verify_uniq(self.get_box(i)):
        return False
 
    return True
        
  '''
  A little bit explaination about how i get the value start
  row = index / 9
  col = index % 9
  blockRow = (row / 3) * 3
  blockCol = (col / 3) * 3
  blockRow = (index / 9 / 3) * 3 = (index / 27) * 3
  blockCol = (index % 9 / 3) * 3
  blockIndex = (blockRow*9) + blockCol = ((index / 27) * 3 * 9) + (index % 9 / 3) * 3  = 
  (index / 27) * 27 + 3 * (index % 9 / 3)
  '''
  def get_box(self, cell): 
    start = 27 * (cell // 27) + 3 * ((cell % 9) // 3)
    indices = [i for j in range(3) for i in range(start + 9 * j, start + 9 * j + 3)]
    result = list()
    for x in indices:
      result.append(self.puzzle[x])
    return result


  def cell_possibilities(self, cell):
    possibilities = set([1,2,3,4,5,6,7,8,9])
    # get row element.
    for i in range(9):
      row = cell//9 * 9 + i
      col = cell%9 + i*9
      possibilities.discard(self.puzzle[row])
      possibilities.discard(self.puzzle[col])
    box = self.get_box(cell)
    for j in box:
      possibilities.discard(j)
    return possibilities


  def assign_cell(self, cell, value):

    self.puzzle[cell] = value

  def unassign_cell(self, cell):

    self.puzzle[cell] = 0
 
  def assign(self):
    # Loop over all the cells.
    for cell in range(81):
  
      # if it's assigned, keep going
      if self.puzzle[cell]: continue
  
      for poss in self.cell_possibilities(cell):
  
        # Assign the cell
        self.assign_cell(cell, poss)
  
        # continue deeper in the recursion.
        if self.assign(): return True
    
        self.unassign_cell(cell)
      return False
  

    return self.verify_solution()




solved, total = 0, 0
with open("sudoku_solved_harder.txt", "w") as out:
  for line in open("sudoku_harder.txt"):

    p = line.strip()
    s = sudoku(p)
    s.assign()

    total += 1
    if s.verify_solution(): solved += 1

    out.write(s.__repr__())

print("Easy {}/{} = {:.3f}".format(solved, total, solved/total))
