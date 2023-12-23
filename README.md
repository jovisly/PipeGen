# Algorithms for Continuous Pipe Generation

I like pipe puzzles ever since I first encountered [Pipe Mania](https://en.wikipedia.org/wiki/Pipe_Mania). There's some mathematical elegance in the setup
of the game. Moreover, it's a simple form of procedural generation, which is
something I had attempted to do for a simple game, using [genetic algorithm](https://github.com/jovisly/MapGen).

How about other algorithms?

## Q Learning

First we use a simple [Q learning](https://en.wikipedia.org/wiki/Q-learning)
algorithm. Starting with randomly generated pipes, we let the agent learn and
update its Q table.

There is no dependency. Although you might need to install [`curses`](https://docs.python.org/3/howto/curses.html) if it's not already in your python version.

```
> python vanilla_q.py
```

https://github.com/jovisly/PipeGen/assets/99686932/17906956-ac6b-47ca-a6cf-85a589c0361c

## Wave Function Collapse

A popular algorithm for procedural generation is [Wave Function Collapse](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/). Typically, the
input is a small image that encapsulates the rules of the pattern. The output is
a much larger (or infinite) image replicated based on such pattern.

Heere we already have the rules described in `utils.py`, so we just assign weights
to the tiles that allow us to pick based on entropy (weights, probability, and
entropy are all related). Then, we can progressively "collapse" the tiles based
on the rules. We can also tune the weights for different density or patterns of
pipes, e.g., proportions between straight pipes vs connectors.

```
> python vanilla_wfc.py
```

https://github.com/jovisly/PipeGen/assets/99686932/768e9db9-e770-4289-982d-16957f73bf80
