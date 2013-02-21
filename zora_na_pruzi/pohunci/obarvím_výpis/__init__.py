from .termcolor.termcolor import colored

def davaj_obarvovací_funkci(barva, pozadí = None,  styl = None,  vypíšu = True,  **parametry_printu):
    
    šablona = colored('{text}',  color = barva,  on_color = pozadí,  attrs = styl)
    
    def obarvi(*args,  **kwargs):
        barevně = []
        for text in args:
#            barevně.append(colored(text,  color = barva,  on_color = pozadí,  attrs = styl))
            barevně.append(šablona.format(text = text))
        if vypíšu:
            parametry = {}
            parametry.update(parametry_printu)
            parametry.update(kwargs)
            print(*barevně,  **parametry)
        else:
            return barevně
    return obarvi
 
import sys,  io
 
def obarvi_print(*args,  barva = None,  pozadí = None, styl = None,   **kwargs):
    if barva is not None or pozadí is not None:
        stdout = sys.stdout
        output_buffer = io.StringIO("")
        sys.stdout = output_buffer
        print(*args,  **kwargs)
        sys.stdout = stdout
        obsah = output_buffer.getvalue().rstrip('\n')
        print(colored(obsah,  color = barva,  on_color = pozadí,  attrs = styl),  **kwargs)
    else:
        print(*args,  **kwargs)
