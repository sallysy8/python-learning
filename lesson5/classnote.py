#
# dict = {'Fred': 200, 'Sally': 70}
#
# for k in dict:
#     print(k)
#
# for v in dict.values():
#     print(v)
#
# for j in tinny:
#     a_list.append(j)
# import random
#     random.choice(a_list)
#
#
# next(iter(tiny))

import itertools
def islice(iterable, *args):
    words = "I wish I may I wish I might".split()
# for w1, w2, w3 in zip(words[:-2], words[1:-1], words[2:]):
#     print(w1,w2, w3)


    l = len(words)
    for w in zip(words, islice(words, 1, None), islice(words, 2, None)):
        print(w)



'''
Mailroom4
'''
def return_to_menu():
    return True

prompt = dedent('''
Choose an action:
1. To send  ''')
run_menu(prompt, selection_dict)

def run_menu(prompt, selection_dict):
    while True:
        selection = inout(prompt).strip().lower()
        try:
            if selection_dict[selection()]:
                break
        except KeyError:
            print()