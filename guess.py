#!/usr/bin/python

from __future__ import division


def rules():
    output = \
        """
    Let's play a game, I will try to guess a number you are thinking about.
    It has to a whole number greater than 1 and n.
    """
    print output
    return int(raw_input('Please enter your a number n.\n'))


def divide_conquer(min, max):
    return (min + max) // 2


def main():

    maximum_number = rules()
    game_memory = {'guess': 0, 'played': 0}
    brain = {'min': 1, 'max': maximum_number}
    gameplay = 'y'
    i = 1
    while True:

        if gameplay == 'y':

            guess = divide_conquer(brain['min'], brain['max'])

            if brain['max'] - brain['min'] == 2:
                response = 'c'
                guess = brain['min'] + 1
            else:
                response = raw_input('Is the number ' + str(guess)
                        + ' . Or is it (H)igher or (L)ower or (C)orrect or (Q)uit \n'
                        )

            if response.lower() == 'c':
                response = ''
                brain = {'min': 1, 'max': maximum_number}
                game_memory['guess'] = i
                game_memory['played'] += 1
                avg = '%.3f' % (game_memory['guess']
                                / game_memory['played'])
                print 'Your number is ' + str(guess)
                print 'I averaged ' + avg + ' guesses per game for ' \
                    + str(game_memory['played']) \
                    + ' game(s). Total number of guess ' \
                    + str(game_memory['guess'])
                gameplay = \
                    raw_input('Do you want to play again (Y)es or (N)o .\n'
                            )
            elif response.lower() == 'h':
                brain['max'] = guess
                i += 1
            elif response.lower() == 'l':
                brain['min'] = guess
                i += 1
            elif response.lower() == 'q':
                gameplay = 'n'
        else:

            print 'Thanks for playing'
            exit()


if __name__ == '__main__':
    main()
