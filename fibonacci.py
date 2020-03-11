from coinflip import coinflip

class Original:
  """The original fibonacci sequence."""
  def __init__(self):
    self.memo = [1, 1]

  def __getitem__(self, index):
    current = len(self.memo)
    while current <= index:
      self.memo.append(self.memo[current - 1] + self.memo[current - 2])
      current += 1
    
    return self.memo[index]

class Random:
  """A random sequence based around a fibonacci style recurrence relation."""

  def __init__(self):
    self._memo = [1, 1]

  def __getitem__(self, index):
    current = len(self._memo)

    while current <= index:
      self._memo.append(
        self._memo[current - 1] +
        (1 if coinflip() else -1) *
        self._memo[current - 2]
      )
      current += 1
    
    return self._memo[index]

