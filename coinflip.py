import random

def coinflip(probabilityOfHeads: float = .5) -> bool:
  """Flip a (fair by default) coin.

  Returns:
    bool: true for heads, false for tails.
  """
  return random.uniform(0, 1) < probabilityOfHeads

