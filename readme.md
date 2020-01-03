Auxiliary documentation about the software is expected to include a simple readme file, 
a licence file and may also include user and developer documentation. 
The readme should either be a markdown format or simple ASCII text file. 
It should provide a contents (a simple list of what all the files/directories are), outline what the software is, 
how it can be run and what is to be expected when it is run, and should point to the licence.) 
Any additional document might provide more details about how to run the software, what to expect when it is run, 
outline any ‘known issues’, outline any testing done and may provide a suggested development roadmap. 

*Files required*

- ABMUnit7.py
- agentframework.py
- in.txt

*Software required*

- A python program - This application was created in Spyder but should run in any python program

* How to run the application*

- save the datafiles required into a directory,
- open a python software and load the ABMUnit7.py file. 
- click run within the python software to load the animated graph and any related text outputs
- N.B. graph and text outputs may load in separate windows dependant on which python software is used

*Expected output*

- the animated model will generate and move the agents around the map for 500 iterations whilst eating the old data 
  and sharing the new data with the other agents. 
- the sharing of data will prevent the agents from colliding and if they become in close proximity of each other or 
  the edge of the map they will automatically move away.
- a text output will also be generated showing the pythagoras theory for a random pair of agents as they moved around.
