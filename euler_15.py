# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.

# 1. r,r,d,d
# 2. r,d,r,d
# 3. r,d,d,r
# 4. d,r,r,d
# 5. d,r,d,r
# 6. d,d,r,r

# How many such routes are there through a 20×20 grid?

#observations

# 1
# the number of moves is equal to the length+width for 
# a single traversal 2x2 = 4, so 20x20 = 40 valid moves

# 2
#20x20 means 40 moves should make it to the end (20 r and 20 d)
#since it's square, that shouldnt change regardless of the order of r's and d's

# 3 
# a 2x2 grid has 6 possible sets of 4 moves, or 24 possible moves.
# 


# i could generate unique combinations of "r" and "d", store them in a set/dict/object/hashtable.
grid = "20x20"
#psuedo crack at it. 
def functionThing(grid):
#start with taking in the grid directions for the grid and figuring out what size it is.
    new = grid.split("x")
    #define the limit
    limit = int(new[0]) + int(new[1]) #limit == 40 //true
    
    directions = ['r','d'] #right and down respectively.
    #end result should be an array (or dictionary) of arrays where each inner array is a unique set of combinations of r and d, with a length of 40.

    #i'll need to make branching decisions based on what comes up. i keep thinking recursion would be good here.
    #start with an empty array.
    outcomes = []
    
    def find_the_thing(n, result=[]):
        #base case, limit has been reached.
        if n <= 0:
            outcomes.append(result)
            return
        #while the list length is less than the limit
        for move in directions:
            #recurse
            find_the_thing(n-1, result+[move])
    
    find_the_thing(limit, [])
    return outcomes       

functionThing(grid)