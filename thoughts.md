# How I want to make this work

## Do all the actions through a command prompt
-Have all the functions execute through the command line
-Dynamically show where entities are being added/referenced to as you type
-Limit using mouse as much as possible
-Maybe have this part written in python?

## Save files in human readable format
-Read from save file and convert to something easier for the computer to understand to make running smoother
-Keep buffer of changes to structure that have been made since the last save
-Try to simplify changes before writing to save file
	-Like if a column gets moved 3m north and then 3m south don't change anything 
	-Or if a column is created and then deleted don't have a ghost column somewhere
-Information I can think of it needing
	-Name/index
		-For referencing from other members
	-Material
	-Start Location
	-End Location
	-Length
	-Mass
	-Suface area?? -For wind calculations
	-Orientation
		-Need to know which side is which
		-Need to know which side is up
		-Give some kind of standard way to know which side you're talking about
	-Member Type
		-one way slab, two way slab, beam, column, shear wall, non-structural wall, roof, etc
		-No idea how I'll implement slabs yet
	-Section
		-Dimensions for concrete
			-Also reinforcement pattern - this will be difficult to specify and model I think
		-Pre-defined shape for steel
		-Dimensions and type of wood for wood
	-Connected to
		-Which members specified member will transmit load into
		-Where the connection is on the member being connected to 
	-Connected from
		-Where the connection is on the specified member
	-Connection type
		-Moment, pin, roller, etc
	-E
	-A
	-Ix
	-Iy
	

## Need some way of getting information on building elements
-Could be just a command to show the attributes of a certain element
-Could also be separate window like in Revit but I don't like that as much
-Show Mf and Mr, Cf and Cr

## Really want to be able to do deformation analysis on the whole structure
-Should look at Samer Adeeb's website on FEA
-Also make sure that the save files contain enough information on connection, material, E, etc to be able to make a good model
-Maybe have a library of the design loads that need to be applied for a certain area?
	-Like have a property of the whole project be the location
	-Also need the soil info I think
	-But use the location info to pick the load cases from the library
	-Just make it so you don't have to calculate earthquake and wind loads separately and input to analysis somehow, have it do that for you
		-As long as it shows what the loads are, where they've been applied, and the resulting deformation I think engineers would be happy
	-Would be nice to be able to cycle through the load cases to be able to see how each one affects the structure differently

