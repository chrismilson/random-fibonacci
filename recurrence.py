class Relation:
  """A recurrence relation based sequence
  
  Args:
    relation (int[], int -> int): A function that can be used to calculate the 
      next value in the sequence given the previous values.
    initial (int[]): An array representing the initial state of the sequence;
      the relation should return the next value in the sequence given this
      array.
    name (str): A human readable name representing the sequence.
  """
  def __init__(self, relation, initial, name=''):
    self._memo = initial
    self.name = name

    def next(target):
      """calculates the next value in the sequence"""
      return relation(self._memo, target)

    self._next = next

  def __getitem__(self, index):
    for target in range(len(self._memo), index + 1):
      self._memo.append(self._next(target))

    return self._memo[index]

  def printFirst(self, n):
    print(
      'The first {} numbers'.format(n),
      ('of {}'.format(self.name) if self.name else ''),
      'are:'
    )

    delimeter = ', ' if n < 30 else ',\n'

    for i in range(n - 1):
      print(self[i], end=delimeter)

    print('and', self[n - 1], end='.\n')