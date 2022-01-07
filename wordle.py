from wordbank import wbank
import random


state = { 'word': '',
          'history' : [],
          'gc' : 0
          }



def userguess(inp, state) -> dict:
    guess = list(inp.upper())
    wo = list(state['word'])
    out = []
    for lg in guess:
        if lg in wo:
            out.append(('yellow', "*" + lg))
        else:
            out.append(('white', lg))
    for i in range(len(guess)):
        if guess[i] == wo[i]:
            out[i] = ('green', "#" + guess[i])
    state['history'].append(out)
    return state
    

def userinput() -> tuple:
    inp = input("[][][][][]")
    inp = inp.strip()
    if len(inp) == 5:
        return True, inp
    else:
        return False, inp


def wordle(state) -> None:
    print("Hello, let's play!")
    print("A * next to a letter means it's in the word, a # means it's in the right place!")
    while True:
        while True:
            valid, inp = userinput()
            if valid:
                break
            else:
                print(f"{inp} wasn't a valid guess, your guess needs to be 5 letters long")
        state = userguess(inp, state)
        state['gc'] += 1
        for h in state['history']:
            print(f"[{']['.join([x[1] for x in h])}]")
        if len([x[0] for x in state['history'][-1] if x[0] == 'green']) == 5:
            print("You win!")
            break
        else:
            if state['gc'] == 5:
                print(f"The word was {state['word']}, you didn't win!")
                break

if __name__ == "__main__":
    while True:
        state = { 'word': random.choice(wbank).upper(),
          'history' : [],
          'gc' : 0
          }
        wordle(state)
        inp = input("Play again? y/n")
        if inp.strip().lower() == "y":
            continue
        else:
            print("Goodbye!  Thanks for playing!")
            break