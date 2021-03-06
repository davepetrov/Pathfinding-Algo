#!/usr/bin/python3
#--------------------#
# MAIN PAGE [RUN THIS]
#    Includes
#         -sortByDistance()
#         -findGoalPath()
#         -A_StartCP()
#--------------------#
# David Petrov
# Completed April 29, 2020 Through May 32, 2020
# A* Pathfinding algorithm Visualizer
#--------------------#

from time import sleep
from node import *
from board import *
import pygame
from display import *
from button import Button
from interactive import interactive
pygame.init()

def sortByDistance(self):
    #IMPLEMENT THIS FUNCTION 
    #SORTS CHECkPOINTS BY CLOSEST DISTANCE TO CURRENT NODE
    pass

def findGoalPath(b, winner, currentOpenSet, currentClosedSet):
    for i in range(len(b.openSet)):
        if b.openSet[i].f < b.openSet[winner].f:
            winner = i
    b.current = b.openSet[winner]
    #FINISHED PATH  #####
    if b.current.isGoal(b): 
        b.finish = True
        temp  = b.current 
        b.path.append(temp)
        b.paths.extend(b.path)
        b.path = b.paths
        skip = False
        print("Path found")
        return True

    set_remove(b.openSet, b.current )
    currentClosedSet.append(b.current);
    neighbors = b.current.neighbors
    
    for i in range(len(neighbors)):
        neighbor = neighbors[i]
        newPath = False
        if neighbor not in currentClosedSet and not neighbor.wall:
            temp_g = b.current.g + 1

            if neighbor in b.openSet:
                if temp_g < neighbor.g: 
                    neighbor.g = temp_g
                    newPath = True
            else:
                neighbor.g = temp_g
                b.openSet.append(neighbor)
                newPath = True
            
            if newPath:
                neighbor.h = neighbor.heuristic(b.goal)
                neighbor.f = neighbor.g + neighbor.h
                neighbor.previous=b.current  

def A_starCP(b):
    cp = 0
    skip=False
    while len(b.openSetsCP[cp])>0:
        b.act = 'work'
        winner = 0
        currentOpenSet = b.openSetsCP[cp]
        currentClosedSet = b.closedSetCP[cp]
        a =0
        if len(b.openSetsCP)>1:
            if cp < len(b.checkpoints):
                for i in range(len(currentOpenSet)):
                    if currentOpenSet[i].f < currentOpenSet[winner].f:
                        winner = i
                b.current = currentOpenSet[winner]
                #FOUND CP #cp  #####
                if b.current.isCP(b.checkpoints[cp]): 
                    b.currentCP +=1
                    b.checkpointsFound[cp] = True
                    b.current.previous=None

                    cp+=1
                    b.paths.extend(b.path)
                    b.openSetsCP[cp][0] = b.current
                    b.openSet = b.openSetsCP[cp]
                    b.closedSetCP.append([])
                    #isplay(b)
                    print("CP FOUND")
                    
                    #####
                else:
                    set_remove(currentOpenSet, b.current)
                    currentClosedSet.append(b.current)
                    neighbors = b.current.neighbors
                    
                    for i in range(len(neighbors)):
                        neighbor = neighbors[i]
                        newPath = False
                        if neighbor not in currentClosedSet and not neighbor.wall:
                            temp_g = b.current.g + 1

                            if neighbor in currentOpenSet:
                                if temp_g < neighbor.g:
                                    neighbor.g = temp_g
                                    newPath = True
                                    
                            else:
                                neighbor.g = temp_g
                                currentOpenSet.append(neighbor)
                                newPath = True
                            
                            if newPath:
                                neighbor.h = neighbor.heuristic(b.checkpoints[cp])
                                neighbor.f = neighbor.g + neighbor.h
                                neighbor.previous=b.current 


            else:
                if findGoalPath(b, winner, currentOpenSet,currentClosedSet): return
        else:
            if findGoalPath(b, winner, currentOpenSet, currentClosedSet): return

        ####
        if not b.finish:
            b.path = []
            temp  = b.current 
            b.path.append(temp)
            while temp.previous:
                b.path.append(temp.previous)
                temp = temp.previous

            e = pygame.event.poll()
            if e.type == pygame.KEYDOWN and e.key== pygame.K_SPACE:
                skip = True
            
            if not skip:
                display(b)
        ####
    else:
        print("No Solution")

    display(b)

def main():
    exit = False
    b=Board(rows,cols)
    b.initilize()
    while True:
        b = interactive(b)
        A_starCP(b)
        b.finish = False

    pygame.quit()
    sys.exit()

main()
