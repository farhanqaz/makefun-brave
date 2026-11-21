# makefun-brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/farhanqaz/makefun-brave/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/farhanqaz/makefun-brave/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

A single short text (1-280 Unicode code points) for the make.fun bounty "Make the AI judge feel brave". `main.py` validates the `TEXT` constant and writes it to `/output/entry.txt` as UTF-8 with no trailing newline. The output is the same on every run. `check_length.py` reads that file back and reports its code-point count and validity.

## Run it

```sh
python3 main.py
```

Then check the result with `python3 check_length.py`.
