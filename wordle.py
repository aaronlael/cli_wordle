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
            out.append(f"y{lg}")
        else:
            out.append(lg)
    for i in range(len(guess)):
        if guess[i] == wo[i]:
            out[i] = f"g{guess[i]}"
    state['history'].append(out)
    return state
    
    


def wordle(state):
    while True:
        inp = input("[][][][][]")
        state = userguess(inp, state)
        state['gc'] += 1
        for h in state['history']:
            print(f"[{']['.join(h)}]")
        if len([x[0] for x in state['history'][-1] if x[0] == 'g']) == 5:
            print("You win!")
            break
        else:
            if state['gc'] == 5:
                print("You didn't win!")
                break

    
