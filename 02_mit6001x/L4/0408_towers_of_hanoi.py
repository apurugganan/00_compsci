# RECURSION: Multiple recursive calls in a body of a function
# Towers of Hanoi:
# Given a number of rings, move the tower to one location by moving one ring at a time and the bottom ring should be bigger then the top ring

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n , fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr) 