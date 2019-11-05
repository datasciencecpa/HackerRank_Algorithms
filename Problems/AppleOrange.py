"""
Function Description

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
Input Format

The first line contains two space-separated integers denoting the respective values of  and .
The second line contains two space-separated integers denoting the respective values of  and .
The third line contains two space-separated integers denoting the respective values of  and .
The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .

Constraints

Output Format

Print two integers on two different lines:

The first integer: the number of apples that fall on Sam's house.
The second integer: the number of oranges that fall on Sam's house. """

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # To solve this problem, need to add value of a to array of apples
    # if value fall within s<=value<=t, then apple falls within the range of the house
    # similar thing can be done with oranges
    numApple = 0
    numOrgange = 0
    for dist in apples:
        value = a + dist
        if (value>=s)  & (value<= t):
            numApple +=1
    for dist in oranges:
        value = b + dist
        if (value>=s) & (value<=t):
            numOrgange +=1
    print (numApple)
    print (numOrgange)
