import random

def randomBool(probabilityOfTrue: float = .5) -> bool:
  """Return a random bool"""
  return random.uniform(0, 1) < probabilityOfTrue

def coinflip(probabilityOfHeads: float = .5) -> str:
  """Flip a (fair by default) coin.

  Returns:
    str: heads or tails.
  """
  return 'heads' if randomBool(probabilityOfHeads) else 'tails'
