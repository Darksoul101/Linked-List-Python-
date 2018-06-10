class Node:
	
	# Creating The Node
	def __init__(self,data):
		self.data = data
		self.next = None

# Starting The Linked-List
class Linked_List:
	
	# Head Is None Which Stores The 1st Node Adder
	def __init__(self):
		self.head = None

	def lengthOfNode(self):
		lengthNode = self.head
		length = 0
		while lengthNode is not None:
			length += 1
			lengthNode = lengthNode.next
		return length

	# This Function Import The Node In First
	def Insert_Head(self,newNode):
		temp_Node = self.head
		self.head = newNode
		self.head.next = temp_Node
		del temp_Node
	
	# Where You Want To Import The Node
	def Insert_At(self,newNode,position):
		if position < 0 or self.lengthOfNode() < position:
			print("Invalid position")
		currentNode = self.head
		currentPosition = 0
		while True:
			if currentPosition == position:
				previousNode.next = newNode
				newNode.next = currentNode 
				break
			previousNode = currentNode
			currentNode = currentNode.next
			position += 1
	
	# This Function Import The Node At Last
	def Insert_End(self,newNode):
		if self.head == None:
			self.head = newNode
		else:
			last_Count = self.head
			while True:
				if last_Count.next == None:
					break
				last_Count = last_Count.next
			last_Count.next = newNode
	
	# Print The Value Of Nodes
	def Print_list(self):
		if self.head == None:
			print("List Is Empty")
			return
		couterNode = self.head
		while True:
			if couterNode == None:
				break
			print(couterNode.data)
			couterNode = couterNode.next
    # Delete The First Node
	def deleteFirst_Node(self):
		FirstNode = self.head
		tempDel_Node = FirstNode.next
		self.head = tempDel_Node
	# Delete The Last Node
	def deleteLast_Node(self):
		if self.head == None:
			print("The List Is Empty")
			return
		lastNode = self.head
		before_last = self.head
		while True:
			if lastNode.next == None:
				before_last.next = None
				break
			before_last = lastNode
			lastNode = lastNode.next

			
myList = Linked_List()

my_list = Node("Yash")

myList.Insert_End(my_list)

my_middel = Node("vardhan")

#myList.Insert_At(my_middel,1)

my_2nd = Node("Singh")

myList.Insert_End(my_2nd)

my_lastbut1 = Node("Programmer")

myList.Insert_Head(my_lastbut1)

myList.deleteLast_Node()

myList.deleteFirst_Node()

myList.Print_list()