# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 20:20:45 2019

@author: Lucy Ewers
"""
'''imports the required functions and modules - csv reads in a datafile, matplotlib is required to make the map/graph, 
    agentframework is a related module required to run the program & random allows for a random number of steps to be taken by each agent.'''
import csv
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import random

'''pythagoras code for any pair of agents - determines the distance between any agent pair - 
    allows the agents to determine proximity to each other'''

def distance_between(agents_row_a, agents_row_b):
    return(((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5
        
    
# Creating lists for agents with random starting locations in a 100x100 grid -creates 10 agents who each move 500 times
num_of_agents = 10
num_of_iterations = 500
neighbourhood = 20
agents = []

#animates map/graph to allow the agents to move through their iterations
figure = matplotlib.pyplot.figure(figsize=(8,8)) 
axis = figure.add_axes([0,0,1,1])

#axis.set_autoscale_on(False)
   
# reads 'in.txt' datafile as CSV and prints value as a float - creates the environment for the agents to move through (raster terrain background)
with open('in.txt',newline='') as f:
    environment = []
    reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)
        '''print(value)'''


#Generates the coordinate pairs for 10 agents using the agentframework module
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
    
#print (agents)

'''updates the animation to allow for continued running of agents through their iterations by moving them, 
eating previous data and sharing new information with other agents'''
carry_on = True
      
def update(frame_number):
    figure.clear()
    global carry_on
        
# Moves the agents one step for 500 iterations & creates a torus grid so agents circle if they reach the edge
    for i in range(num_of_agents):
        #for j in range(num_of_iterations):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        #agents[i].shuffle()
        #print (agents)
    if random.random()< 0.1:
        carry_on= False
         
       
#plotting coordinates as a graph - plots each agent on graph and allows for the animation to run
    matplotlib.pyplot.xlim(0, 100)
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

    matplotlib.pyplot.show()
    
def gen_function(b =[0]):
     a =0 
     global carry_on
     while (a<num_of_iterations) & (carry_on):
         yield a
         a = a + 0.5


animation = matplotlib.animation.FuncAnimation(figure, update, repeat=False, frames=gen_function)    

   
'''2nd part of pythagoras calcuation for distance between agents linking to def at start - 
this allows the agents to determine proximity to each other and move away if required when they share data'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
   # print(distance)
    

'''prints a text output to show the agents are moving. initially prints the starting coordinate pair then prints 
the new coordinates after the agent has moved once, this could be repeated for any number of moves.'''
a = agentframework.Agent(environment,agents)
print ('starting coordinates =')
print (a.y, a.x)
a.move()
print ('new coordinates =')
print (a.y, a.x)


