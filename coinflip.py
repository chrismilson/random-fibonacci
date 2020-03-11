import random

def coinflip(probabilityOfHeads: float = .5):
  """Flip a coin (fair by default)

  Returns a boolean where true represents heads.
  """
  return random.uniform(0, 1) < probabilityOfHeads

