import turtle, math, random, time

COORDINATES = []

class Person:
	def __init__(self, x, y):
		self.xCoordinate = x
		self.yCoordinate = y

# This function is used to save the coordinates in a .txt file
def SaveFile(COORDINATES):
	with open('Coordinates.txt', 'w') as f:
		for i in COORDINATES:
			f.write(i, ', ')


# This function is used to sort the coordinates using quick sort

def partition(arr,low,high): 
	i = ( low-1 )           # index of smaller element 
	pivot = arr[high][0]    # pivot 

	for j in range(low , high): 
  
        # If current element is smaller than the pivot 
		if   arr[j][0] < pivot: 
          
			# increment index of smaller element 
			i = i+1 
			arr[i][0], arr[j][0] = arr[j][0], arr[i][0] 
  
	arr[i+1], arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

def QuickSort(coordinates, low, high):
	if low < high:
		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(coordinates,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		QuickSort(coordinates, low, pi-1) 
		QuickSort(coordinates, pi+1, high) 


# This function is used to find out if the current corrdinates collide with any
# previously picked coordinates
# This will cluster them using binary search and comparing the x-axis and
# then making a sub list of all the values which will be much more efficient to
# run through

def BinarySearch(DataSet, xAxis):
	lowerPointer = 0
	upperPointer = len(DataSet)-1
	middlePointer = (lowerPointer+upperPointer)/2
	found = False

	while not found and upperPointer > lowerPointer:
		middlePointer =int((lowerPointer+upperPointer)/2)
		if DataSet[middlePointer][0] == xAxis:
			found = True 
			return middlePointer

		elif DataSet[middlePointer][0] < xAxis:
			lowerPointer = middlePointer + 1

		else:
			upperPointer = middlePointer - 1

	return False

def FindSubSet(index, DataSet, xAxis):
	SubDataSet = []
	if index == False:
		return False, SubDataSet

	# This is finding the start of the list
	else:
		while DataSet[index] == xAxis:
			index -= 1

	while DataSet[index] == xAxis:
		SubDataSet.append(DataSet[index])
		index += 1

	return index, SubDataSet


def FindIfCollision(index, DataSet, coordinates):
	collision = False
	if index == False:
		collision = False
	else:
		for i in range(len(DataSet)):
			if DataSet[i][0] == coordinates[0] and DataSet[i][1] == coordinates[1]:
				collision = True
				break
			else:
				continue

	return collision


# This function finds out all the four possible connections for a specific node
def GetPossiblePeople(coordinates):
	PossiblePeople = [[coordinates[0]+2, coordinates[1]], [coordinates[0]-2, coordinates[1]], [coordinates[0], coordinates[1]+2], [coordinates[0], coordinates[1]-2]]
	return PossiblePeople

def PlotPoint(window, pen, x, y):
	pen.pencolor('blue')
	pen.goto(x, y)
	pen.dot()
	pen.penup()

# This is the main simulation
def Simulate():
	global time
	# Turtle setup
	turtle.setup(1000, 1000)
	window = turtle.Screen()
	window.bgcolor('white')
	t = turtle.Turtle()
	t.hideturtle()



	# Actual simulation
	StartCoords = [0, 0]
	COORDINATES.append(StartCoords)
	NoOfNodes = len(COORDINATES)

	currentCoordinate = StartCoords
	primaryTime = time.time()

	while NoOfNodes < 7594000000:
		QuickSort(COORDINATES, 0, len(COORDINATES)-1)
		possiblePeople = GetPossiblePeople(currentCoordinate)
		for i in range(len(possiblePeople)):
			print(NoOfNodes)
			index = BinarySearch(COORDINATES, possiblePeople[i][0])
			index, subDataSet = FindSubSet(index, COORDINATES, possiblePeople[i][0])
			collision = FindIfCollision(index, subDataSet, possiblePeople[i])
			if collision == False:
				COORDINATES.append(possiblePeople[i])
				NoOfNodes += 1
				PlotPoint(window, t, possiblePeople[i][0], possiblePeople[i][1])
			else:
				continue
	time = time.time()
	print(time-primaryTime)
	turtle.done()

Simulate()