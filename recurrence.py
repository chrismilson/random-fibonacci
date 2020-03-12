class Relation:
  """A recurrence relation based sequence
  
  Args:
    relation (int[], int -> int): A function that can be used to calculate the 
      next value in the sequence given the previous values.
    initial (int[]): An array representing the initial state of the sequence;
      the relation should return the next value in the sequence given this
      array.
  """
  def __init__(self, relation, initial):
    self._memo = initial

    def next(target):
      """calculates the next value in the sequence"""
      return relation(self._memo, target)

    self._next = next

  def __getitem__(self, index):
    for target in range(len(self._memo), index + 1):
      self._memo.append(self._next(target))

    return self._memo[index]
