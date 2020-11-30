# Tower of Hanoi Solver by Maria Regina Sirilan
# Recursively prints instructions for solving the Tower of Hanoi with
# either 3 or 4 pegs and n >= 1 disks (recommended: n <= 6)


def solve3(n, start, end, aux, steps=None):
    """(int, str, str, str) -> list of str

    (3 pegs, n disks)

    Given n disks and labels for the start, end, and auxiliary pegs,
    return a list of steps to move the disks from the start to the end.
    """
    if steps is None:
        steps = []
    if n == 1:
        steps.append('Move from peg ' + start + ' to peg ' + end + '.')
    else:
        # Move the top n-1 disks from start to aux
        solve3(n-1, start, aux, end, steps)
        # Move the bottom disk from start to end
        steps.append('Move from peg ' + start + ' to peg ' + end + '.')
        # Move the n-1 disks from aux to end
        solve3(n-1, aux, end, start, steps)
    return steps


def solve4(n, start, end, aux1, aux2, steps=None):
    """(int, int) -> list of str

    (4 pegs, n disks)

    Given n disks and labels for the start, end, and 2 auxiliary pegs,
    return a list of steps to move the disks from the start to the end.
    """
    if steps is None:
        steps = []
    if n == 1:
        steps.append('Move from peg ' + start + ' to peg ' + end + '.')
    elif n == 2:
        # Move the top n-1 disks from start to aux1
        solve4(n-1, start, aux1, end, aux2, steps)
        # Move the bottom disk from start to end
        steps.append('Move from peg ' + start + ' to peg ' + end + '.')
        # Move the n-1 disks from aux1 to end
        solve4(n-1, aux1, end, aux2, start, steps)
    else:
        # Move the top n-2 disks from start to aux1
        solve4(n-2, start, aux1, aux2, end, steps)
        # Move the n-1 disk from start to aux2
        steps.append('Move from peg ' + start + ' to peg ' + aux2 + '.')
        # Move the bottom disk from start to end
        steps.append('Move from peg ' + start + ' to peg ' + end + '.')
        # Move the n-1 disk from aux2 to end
        steps.append('Move from peg ' + aux2 + ' to peg ' + end + '.')
        # Move the top n-2 disks from aux1 to end
        solve4(n-2, aux1, end, start, aux2, steps)
    return steps


if __name__ == '__main__':

    print('TOWER OF HANOI SOLVER')

    pegs = input('Number of pegs (3 or 4): ')
    while pegs not in ('3', '4'):
        pegs = input('Number of pegs (3 or 4): ')
    disks = input('Number of disks (integer 1 or greater): ')
    while not disks.isnumeric() or int(disks) < 1:
        disks = input('Number of disks (integer 1 or greater): ')

    print('-'*70)
    print('[ SOLUTION ]')

    if int(pegs) == 3:
        soln = solve3(int(disks), '1', '3', '2')
    else:
        soln = solve4(int(disks), '1', '4', '2', '3')

    counter = 1
    for s in soln:
        print(str(counter) + ') ' + s)
        counter += 1
