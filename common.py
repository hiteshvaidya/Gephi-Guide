#This code finds common nodes/intersection between clusters in a graph imported in 'gephi' software

from java.awt import Color

ip = open("nodes.txt", "r")						#file containing names of nodes whose intersection is to be found
nodes = []
col = ip.readline().strip()						#colour to be assigned to common nodes
first_flag = True								#Flag to ignore the first line of the nodes.txt file.

for row in ip:									#start reading nodes.txt
	if first_flag == True:						#read first line containing colour name and ignore it in later iterations
		first_flag = False
		continue
	tmp = row.strip().split(' ')
	nodes.append("v"+tmp[0].strip())			#append 'v' to label name, because by default gephi requires so to do any operation on a node.
ip.close()										#close the nodes.txt file

nbrs = []										#list of neighbours of all the nodes whose intesection is to be found
for node in nodes:
	temp = set([])								#temporary variable that stores the set of neighbours of a node
	node = locals()[node.strip()]				#mapping that converts node name from string to gephi object
	for nbr in node.neighbors:
		temp.add(nbr.label)						#adds all the neighbours of a node to the temp set
	nbrs.append(temp)							#appends temp set to nbrs list

common = "none"									#this will contain all the common nodes/intersection between required nodes
try:											#if there is any common node then try block will run else except block will run
	common = reduce((lambda x,y: x&y), nbrs)	#finds intersection between all the sets of neighbours
	print "common nodes are: "					
	for nd in common:
		print str(nd) + " " + col
		tmp = locals()["v"+nd]
		if col == "black":						#if-else ladder that colours the common nodes by matching the colour mentioned in nodes.txt
			tmp.color = Color.black
		elif col == "blue":
			tmp.color = Color.blue
		elif col == "cyan":
			tmp.color = Color.cyan
		elif col == "darkgray":
			tmp.color = Color.darkgray
		elif col == "gray":
			tmp.color = Color.gray
		elif col == "green":
			tmp.color = Color.green
		elif col == "yellow":
			tmp.color = Color.yellow
		elif col == "lightgray":
			tmp.color = Color.lightgray
		elif col == "magenta":
			tmp.color = Color.magenta
		elif col == "orange":
			tmp.color = Color.orange
		elif col == "pink":
			tmp.color = Color.pink
		elif col == "red":
			tmp.color = Color.red
		elif col == "white":
			tmp.color = Color.white
except:											#if no common node found then simply a message would be displayed
	print("no common nodes found")
