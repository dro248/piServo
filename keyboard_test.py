from curtsies import Input

with Input(keynames='curses') as input_generator:
    for e in input_generator:
        if repr(e) == "u'KEY_LEFT'" or repr(e) == "u'KEY_RIGHT'":
            print(repr(e))
        
