# Reinforcement Learning for Continuous Pipe Generation

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
