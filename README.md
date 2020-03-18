# MineSweeper
A mine sweeper game, but wait a sec... Its not like mine sweeper games you've played before

You must write your map like this

<br/>
  
    ...
    ..*
    .*.
    
You must type \'*\' for mines and '.' for free spaces.

It will show you how many mines are around free spaces

    0 1 1
    1 2 *
    1 * 2
    
## How to use
Run mineSweeper.py

    mine-sweeper> python mineSweeper.py
    
### Input
In the first, you must choose how many lines do your map have and how much length every line have.

    Enter lines count:  3
    Enter lines length: 3
    
In above example we have 3 lines and every line have 3 character

Now as what you entered, you must type your map

    Enter line 01: ...
    Enter line 02: ..*
    Enter line 03: .*.
    
Like what I've choosed, I type 3 line and every line has 3 character

### Output

    Dot Map:
    . . .
    . . *
    . * .
    Num Map:
    0 1 1
    1 2 *
    1 * 2
