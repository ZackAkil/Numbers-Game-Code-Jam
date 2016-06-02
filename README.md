# Number Game Code Jam
Solution to the number game puzzle from [google code jam Round 1A 2010](https://code.google.com/codejam/contest/544101/dashboard#s=p2)

##The problem
Arya and Bran are playing a game. Initially, two positive integers A and B are written on a blackboard. The players take turns, starting with Arya. On his or her turn, a player can replace A with A - k*B for any positive integer k, or replace B with B - k*A for any positive integer k. The first person to make one of the numbers drop to zero or below loses.

For example, if the numbers are initially (12, 51), the game might progress as follows:

- Arya replaces 51 with 51 - 3*12 = 15, leaving (12, 15) on the blackboard.
- Bran replaces 15 with 15 - 1*12 = 3, leaving (12, 3) on the blackboard.
- Arya replaces 12 with 12 - 3*3 = 3, leaving (3, 3) on the blackboard.
- Bran replaces one 3 with 3 - 1*3 = 0, and loses.

We will say (A, B) is a winning position if Arya can always win a game that starts with (A, B) on the blackboard, no matter what Bran does.

Given four integers A1, A2, B1, B2, count how many winning positions (A, B) there are with A1 ≤ A ≤ A2 and B1 ≤ B ≤ B2.

##Solution theory
The script initially brute forced each possible game scenario to see if it was a win or a lose for Arya using a observed winning logic of:
Whoever is the first to "get a choice of multiple moves were the output of the moves do not give the next player the same choice" is the winner, otherwise play the "forced" game to the end to see who is the winner.

The approach above is however too slow to compute the large data set in time. Therefore the code was used to generate the outputs of sequential game scenario (e.g [1,10],[2,10],[3,10] etc) in order to perform data analysis to find a trend which can be exploited for solving the problem faster. Discovered was a trend (shown in the graph below) which involved multiplying the number in a game scenario by the golden ratio (1.6180) which would give the upper bounds of when it would start losing games for that players turn. The lower bounds is equal to the upper bounds - the number itself. This “losing range” is then subtracted from the game scenario ranges were it intersects which produced the total number of winning games.

![Number game data chart][chart]

[chart]: /number-game-data.png "Number game data chart"

##Usage
To use the solution: run the python script from a terminal passing it the name of the input file followed by the desired name of the output file.   

```
$ /User python numbers.py C-small-practice.in small-output.out
```
