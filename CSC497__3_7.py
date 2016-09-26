import math

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

	def balanced(self, other):
		return self.cannibalLeft == other.cannibalLeft and self.missionaryLeft == other.missionaryLeft \
                   and self.boat == other.boat and self.cannibalRight == other.cannibalRight \
                   and self.missionaryRight == other.missionaryRight

	def _hash(self):
		return hash((self.cannibalLeft, self.missionaryLeft, self.boat, self.cannibalRight, self.missionaryRight))

		
# Here we create the potential groupings and movements that are allowed within the boundaries of the problem. We
# begin with an initial state of user input for cannibals and missionaries, (num_cannibals = num_missionaries)
# and establish the boat to be on the left side of the river. 

def successors(current_state):
	children = [];
	if current_state.boat == 'left':
		new_State = State(current_state.cannibalLeft, current_state.missionaryLeft - 2, 'right',
                                  current_state.cannibalRight, current_state.missionaryRight + 2)
								  
		# Two missionaries cross from left to right.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft - 2, current_state.missionaryLeft, 'right',
                                  current_state.cannibalRight + 2, current_state.missionaryRight)
								  
		# Two cannibals cross from left to right.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft - 1, current_state.missionaryLeft - 1, 'right',
                                  current_state.cannibalRight + 1, current_state.missionaryRight + 1)
								  
		# One missionary and one cannibal cross from left to right.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft, current_state.missionaryLeft - 1, 'right',
                                  current_state.cannibalRight, current_state.missionaryRight + 1)
								  
		# One missionary crosses from left to right.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft - 1, current_state.missionaryLeft, 'right',
                                  current_state.cannibalRight + 1, current_state.missionaryRight)
								  
		# One cannibal crosses from left to right.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
	else:
		new_State = State(current_state.cannibalLeft, current_state.missionaryLeft + 2, 'left',
                                  current_state.cannibalRight, current_state.missionaryRight - 2)
								  
		# Two missionaries cross from right to left.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft + 2, current_state.missionaryLeft, 'left',
                                  current_state.cannibalRight - 2, current_state.missionaryRight)
								  
		# Two cannibals cross from right to left.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft + 1, current_state.missionaryLeft + 1, 'left',
                                  current_state.cannibalRight - 1, current_state.missionaryRight - 1)
								  
		# One missionary and one cannibal cross from right to left.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft, current_state.missionaryLeft + 1, 'left',
                                  current_state.cannibalRight, current_state.missionaryRight - 1)
								  
		# One missionary crosses from right to left.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
		new_State = State(current_state.cannibalLeft + 1, current_state.missionaryLeft, 'left',
                                  current_state.cannibalRight - 1, current_state.missionaryRight)
								  
		# One cannibal crosses from right to left.
		if new_State.valid():
			new_State.parent = current_state
			children.append(new_State)
			
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print "(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                              + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                              str(state.missionaryRight) + ")"

def main():
	solution = breadth_first_search()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	print_solution(solution)

# if called from the command line, call main()
if __name__ == "__main__":
    main()
