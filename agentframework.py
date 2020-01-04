# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 15:39:05 2019

@author: Lucy Ewers
"""
import random

class Agent():
    def __init__ (self, environment,agents):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        self.environment = environment
        self.store = 0
        self.agent = agents
        self.store = 0
          
    def move(self):   
        if self.x < 50:
            self.x = (self.x  + 5) % 100
        else:
            self.x  = (self.x  - 5) % 100

        if self.y < 50:
            self.y = (self.y + 5) % 100
        else:
            self.y = (self.y - 5) % 100
            
    def eat(self):
        if self.environment[self.y][self.x] > 5:
            self.environment[self.y][self.x] -= 5
            self.store += 5
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agent:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average = ((self.store + agent.store)/2)
                self.store = average
                agent.store = average
                #print("sharing " + str(distance) + " " + str(average))
    
    def distance_between(self, agent):
        return(((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5        
        
