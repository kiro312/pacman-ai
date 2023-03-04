import os
def DFS():
    os.system("python pacman.py -l mediumMaze -p SearchAgent")

def BFS():
    os.system("python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs")

def UCS():
    os.system("python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs")

def AStarFunction():
    os.system("python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic")

def GBFS():
    os.system("python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=gbfs,heuristic=manhattanHeuristic")

from tkinter import *       

from tkinter.ttk import *

root = Tk()
           
root.geometry('250x200')
 
btn1 = Button(root, text = 'DFS ', command = DFS,)

btn2 = Button(root, text = 'BFS', command = BFS)

btn3 = Button(root, text = 'UCS', command = UCS)

btn4 = Button(root, text = 'A*', command = AStarFunction)

btn5 = Button(root, text = 'GBFS', command = GBFS)
 
# Set the position of button on the top of window
btn1.pack(side = 'top')
btn2.pack(side = 'top')
btn3.pack(side = 'top')
btn4.pack(side = 'top')
btn5.pack(side = 'top')
 
root.mainloop()