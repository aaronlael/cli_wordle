# cli_wordle
A very dirty python implementation of wordle


```python
>>> state['word'] = 'tacos'.upper()
>>> wordle(state)
[][][][][]farts
[F][gA][R][yT][gS]
[][][][][]tacos
[F][gA][R][yT][gS]
[gT][gA][gC][gO][gS]
You win!

```


To do list:
 - validate user input length/trim whitespace
 - move g,y into parallel list and implement library for cli coloring
 - implement wordbank
 - implement proper gameloop with if __name__ == __main__:
