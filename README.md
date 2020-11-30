<!-- TITLE -->
# 🧩 Tower of Hanoi

<b>towerofhanoi.py</b> is a playable, text-based <a href="https://en.wikipedia.org/wiki/Tower_of_Hanoi">Tower of Hanoi</a> game written in Python. Short, input-based commands make it easier to move disks between pegs as opposed to a graphical UI.

<b>hanoisolver.py</b> is a solution generator that recursively lists steps to solve a Tower of Hanoi puzzle in the lowest possible number of moves (e.g., <i>2<sup>n</sup>-1 for 3 pegs</i>). Supports 3 or 4 pegs and any number of disks.

<!-- USAGE -->
## 🛠 Usage
<b>towerofhanoi.py</b> requires <a href="https://numpy.org/">NumPy</a> - though I might add extra functionality later so that this isn't necessary!

<b>Example:</b> enter <b>13</b> to move a disk from peg 1 to peg 3
```
[ SETTINGS ]
> Please enter a number of disks (3-9): >? 4
----------------------------------------------------------------------
	   1		   -		   -
	   2		   -		   -
	   3		   -		   -
	   4		   -		   -
	[- 1 -]		[- 2 -]		[- 3 -]
> Moves: 0 | Enter a move: 13
----------------------------------------------------------------------
	   -		   -		   -
	   2		   -		   -
	   3		   -		   -
	   4		   -		   1
	[- 1 -]		[- 2 -]		[- 3 -]
> Moves: 1 | Enter a move:   
```

<b>hanoisolver.py</b> example for generating a list of moves for 3 pegs with 4 disks:
```
TOWER OF HANOI SOLVER
Number of pegs (3 or 4): 3
Number of disks (integer 1 or greater): 4
----------------------------------------------------------------------
[ SOLUTION ]
1) Move from peg 1 to peg 2.
2) Move from peg 1 to peg 3.
3) Move from peg 2 to peg 3.
4) Move from peg 1 to peg 2.
5) Move from peg 3 to peg 1.
6) Move from peg 3 to peg 2.
7) Move from peg 1 to peg 2.
8) Move from peg 1 to peg 3.
9) Move from peg 2 to peg 3.
10) Move from peg 2 to peg 1.
11) Move from peg 3 to peg 1.
12) Move from peg 2 to peg 3.
13) Move from peg 1 to peg 2.
14) Move from peg 1 to peg 3.
15) Move from peg 2 to peg 3.
```

<!-- CONTRIBUTING -->
## 💘 Contributing
All efforts to improve efficiency, documentation, and other aspects are greatly appreciated!
