# Random Fibonacci

This is a project based on [the youtube video on the same
topic](https://www.youtube.com/watch?v=ELA8gNNMHoU).

## Background

The fibonacci sequence is a sequence of integers F<sub>n</sub> where:

- F<sub>0</sub> = F<sub>1</sub> = 1.
- F<sub>n</sub> = F<sub>n - 1</sub> + F<sub>n - 2</sub> for n ≥ 2.

A random fibonacci sequence is similar, however instead of adding (n - 1)<sup>th</sup> and
(n - 2)<sup>th</sup> value to get the m<sup>th</sup> value, there is a chance that the n<sup>th</sup> value is
the (n - 1)<sup>th</sup> value ***minus*** the (m - 2)<sup>th</sup> value.

Alternatively, we can define a special fibonacci sequence R<sub>β,n</sub> for
every binary sequence β: ℕ → {0, 1} where:

- R<sub>β,0</sub> = R<sub>β,1</sub> = 1
- R<sub>β,n</sub> =
  - R<sub>β,n - 1</sub> + R<sub>β,n - 2</sub> if β<sub>n - 2</sub> = 1,
  - R<sub>β,n - 1</sub> - R<sub>β,n - 2</sub> if β<sub>n - 2</sub> = 0

*NOTE: The offset of 2 in β<sub>n - 2</sub> is so that there is a natural
bijection between binary sequences and special fibonacci sequences.*

*ALSO NOTE: The original fibonacci sequence is R<sub>β,n</sub> where β is the
binary sequence containing only 1's*