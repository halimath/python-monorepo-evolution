# RPG dice roller

This notebook demonstrates how we can develop a roleplaying game dice roller.

# Input specs

A RPG dice roller expression follows the following syntax:

```
[<dice count>]d<die num>[(+|-)<mod>]
```

* `dice count` is an optional (positive) number defining how many dice to roll (or how often to roll a single die and sum up the results)
  This number is optional. If not given defaults to 1.
* `die num` defines the number of sides the die must have. Valid numbers are 2, 3, 4, 6, 8, 10, 12, 20, 50 and 100
* `mod` defines a modifier to apply - a fixed number to either add or subtract from the die/dice roll result.
  `mod` and its preceding sign are optional (either sign and number are given or none of them). If no modifier has been given it defaults to 0.

## Examples

* `d20` means to roll a single 20-sided die
* `d20+2` means to roll a single 20-sided die and add `2` to the result
* `3d8-5` means to roll three eight-sided dice, add their numbers and subtract `5` from the result

# Natural result

For some of the rolls it is important to know what the _natural result_ is. The natural result is the result of the die/dice w/o applying the modifier.
I.e. when rolling `d20+2` a _natural one_ is ususally considered a _disaster_ where a _natural 20_ is a _triumphal success_.