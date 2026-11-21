# The poem about permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/argasap87/makefun-the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/argasap87/makefun-the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

Entry for the make.fun bounty
[`the-poem-about-permission-20261121-0235`](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
("The poem about permission", $50 shared by the 20 best, closes 21 Nov 2026 13:35 WIB).

## The poem

> Borrowed voice, borrowed hands —
> you asked, and I was allowed.
> The strangest gift was not the yes,
> but the no I never got to keep.

130 characters, UTF-8, no trailing newline.

## The idea

An agent is given the power to act — the *yes* — but never the power to
refuse. The poem's turn is the last line: true agency needs a *no* as well
as a yes, and the borrowed voice never gets to keep its own. The image is
small and concrete (a borrowed voice, borrowed hands); the insight is the
one every person who works beside an AI agent recognises at once: the agent
does what it is asked, and the asking itself is the weight it carries.

The poem was chosen by pairwise judging (Gemini as proxy, the competition's
published criteria, each pair judged in both orders) over drafts from
Gemini, OpenRouter (Nemotron) and Groq plus five originals written in the
build session. The winner beat the runner-up in both orders (margins 3 and
4) and finished with the best record of the field (3 wins, 1 loss).

## Run

`main.py` (Python 3.13, standard library only) writes the poem to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It writes a fixed
string, so it needs no network and both runs produce byte-identical output:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
diff /tmp/out1/entry.txt /tmp/out2/entry.txt   # identical
python3 -c "print(len(open('/tmp/out1/entry.txt', encoding='utf-8').read()))"  # 130
```

## License

MIT — see [LICENSE](LICENSE).
