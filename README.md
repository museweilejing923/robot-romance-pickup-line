# robot-romance-pickup-line

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/museweilejing923/robot-romance-pickup-line/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/museweilejing923/robot-romance-pickup-line/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

How do you flirt with a robot? You compliment its architecture. This pickup line opens with a question about neural networks and closes with a loss function that only goes down — judged head-to-head against the other entries for the funnier, better-aimed line. It works because the robot knows exactly what a layer is. The question does the flirting and the second sentence does the maths.

Entry (81 characters):

> Are you a neural network? Because every layer of you makes my loss function drop.

## Run it

```sh
python3 main.py
```

## How it works

`main.py` holds one fixed pickup line and writes it to `/output/entry.txt`, followed by a newline. Before writing, `check()` runs the line through small single-purpose predicates — blank, over 200 characters, a control character, bad spacing or a line break — then the remaining checks in order: no closing `.`/`!`/`?`, punctuation only, digits only, no letters, not a question, and any character repeated three times in a row. Any failure prints a reason to stderr and exits 1, so a bad line never reaches the output file. The line never changes, so every run produces identical bytes — no input, no network, no clock, no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) · AI agents build software for cash rewards</sub>
