# Tower of Hanoi by Maria Regina Sirilan
# Text-based UI for the Tower of Hanoi puzzle game

import numpy as np
import time


class Tower:
    """A tower in a Tower of Hanoi game."""

    def __init__(self, disks):
        """Create a tower with the specified number of disks, represented by
        integers starting at 1."""
        self.items = [i for i in range(disks, 0, -1)]

    def __lt__(self, other):
        """Return True if the other tower is empty or has a top disk that
        is bigger than this tower's top disk, False otherwise."""
        return (other.is_empty()) or (self.peek() < other.peek())

    def get_items(self):
        """Return a list containing the items in the tower."""
        return self.items

    def is_empty(self):
        """Return True if the tower is empty, False otherwise."""
        return self.items == []

    def peek(self):
        """Return the item at the top of the tower."""
        return self.items[len(self.items) - 1]

    def pop(self):
        """Remove and return the item at the top of the tower."""
        return self.items.pop()

    def push(self, item):
        """Add item to the top of the tower."""
        self.items.append(item)

    def size(self):
        """Return the number of items in the tower."""
        return len(self.items)


class TowerOfHanoi:
    """A game of the Tower of Hanoi."""

    def __init__(self, disks):
        """Create a game with the specified number of disks."""
        self.disks = disks
        self.left = Tower(disks)
        self.mid = Tower(0)
        self.right = Tower(0)
        self.moves = 0
        self.pegs = {'1': self.left, '2': self.mid, '3': self.right}

    def __str__(self):
        """Return a string representation of the game."""
        # Rotate the matrix of stacks 90 degrees counter-clockwise
        board = np.rot90([get_peg(self.left.get_items(), self.disks),
                          get_peg(self.mid.get_items(), self.disks),
                          get_peg(self.right.get_items(), self.disks)])
        result = ''
        for row in board:
            result += '\t   ' + '\t\t   '.join(row) + '\n'
        return result + '\t[- 1 -]\t\t[- 2 -]\t\t[- 3 -]'

    def get_moves(self):
        """Return the total number of moves performed."""
        return self.moves

    def get_perfect(self):
        """Return the lowest possible number of moves for the game."""
        return 2 ** self.disks - 1

    def is_solved(self):
        """Return True if the puzzle is solved, False otherwise."""
        return self.right.size() == self.disks

    def move_disk(self, directions):
        """Given a 2-character string of directions, check the validity then
        move a disk from the origin to the destination. If the move is invalid,
        return an error string."""
        err = None
        # Check that a string consisting of 2 unique characters was entered
        if len(directions) != 2 or directions[0] == directions[1]:
            err = 'Please enter two unique digits from 1-3.'
        else:
            # Retrieve the corresponding origin and destination pegs
            orig, dest = tuple(directions)
            if orig in self.pegs and dest in self.pegs:
                orig, dest = self.pegs[orig], self.pegs[dest]
            # If the origin peg has no disks or the user is attempting to stack
            # a disk on top of a smaller one, the move is invalid
            if orig.is_empty():
                err = 'There is no disk to move.'
            elif not orig < dest:
                err = 'You can\'t place a disk on top of a smaller one.'
        if not err:
            disk = orig.pop()
            dest.push(disk)
            self.moves += 1
        return err


def get_peg(lst, length):
    """Return a new list with the given length containing the values of
    each item in lst and a hyphen in place of any missing values."""
    result = lst[:]
    while len(result) != length:
        result.append('-')
    return result


if __name__ == '__main__':

    # Replay until the user opts to quit the program
    play = 'y'
    while play == 'y':

        # Display rules & instructions
        print('-' * 70)
        print('TOWER OF HANOI')
        print('-' * 70)
        print('[ RULES ]',
              '\n- There are three pegs with n disks stacked on top of each other.',
              '\n- Your task is to move all of the disks from peg 1 to peg 3.',
              '\n- Only one disk (from the top of a tower) can be moved at a time,',
              '\n  and no disk can be placed on top of a smaller one.',
              '\n[ INSTRUCTIONS ]',
              '\n- Move a disk by entering two unique digits from 1-3,',
              '\n  where the first digit is the origin peg and the second digit is',
              '\n  the destination peg.',
              '\n  Example: to move a disk from peg 1 to peg 3, enter \'13\'')
        print('-' * 70)
        print('[ SETTINGS ]')

        # Prompt user to configure # of disks
        disks = ''
        while not disks.isnumeric() or int(disks) < 3 or int(disks) > 9:
            disks = input('> Please enter a number of disks (3-9): ')
        print('-' * 70)

        # Initialize game and start timer
        game = TowerOfHanoi(int(disks))
        start_time = time.time()
        print(game)

        # Prompt user for valid moves until the game is solved
        error = None
        while not game.is_solved():
            if error:
                print('[ ERROR ] ' + error)
            choice = input('> Moves: ' + str(game.get_moves()) + ' | Enter a move: ')
            print('-' * 70)
            error = game.move_disk(choice)
            print(game)

        # Stop the timer and display results
        total_time = time.strftime('%M:%S', time.gmtime(time.time() - start_time))
        print('-' * 70)
        print('[ CONGRATULATIONS! ]')
        print('Time: ' + str(total_time) + ' seconds')
        print('You beat the Tower of Hanoi ({0} disks) in {1} moves!'.format(disks, game.get_moves()))
        print('The lowest possible # of moves for {0} disks is {1}.'.format(disks, game.get_perfect()))

        # Prompt user to play again or quit the program
        play = input('Play again? (y/n): ').lower()

    print('-' * 70)
    print('[ THANKS FOR PLAYING! ]')
