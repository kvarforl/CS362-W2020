# -*- coding: utf-8 -*-
"""
Created on Sunday January 12

@author: kvarforl
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names


player_names = ["Annie","*Ben","*Carla"]
curses, victories = testUtility.getCursesAndVictories(player_names)
box = testUtility.createBox(victories)
player_names.append("Susan") #this line will introduce a bug
supply, supply_order = testUtility.initSupply(box, player_names)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.createPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)