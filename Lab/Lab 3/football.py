"""
Title: Football
Description:
	Define a class called “Ball” which defines the position of the ball by using x,y positions
	[x-coordinate, y-coordinate] and delta-x, delta-y which gives the amount change in x-direction and
	y-direction respectively.
	Define another class called “MyFavGame” which inherits the “Ball” class has dimensions
	of ground, goal posts and has methods to move the ball in the ground, into the posts and
	maintains score. You get a point if you move the ball into the goal posts and lose a point
	if your ball moves out of the ground. Also give yourself a minimum of 5 moves and print the
	score you get after that.
Author: akashroshan135
Date: 25-Feb-2021
"""

class ball():
	# sets ball to center of the ground
	def newBall(self, x, y):
		self.x_pos = x
		self.y_pos = y

	# moves the ball's position
	def ball_move(self, x, y):
		self.x_pos += x
		self.y_pos += y

	# prints the ball's current position
	def give_ball_pos(self):
		print('Ball\'s X position =', self.x_pos)
		print('Ball\'s Y position =', self.y_pos)

class MyFavGame(ball):
	# coordinates for the ground, can be altered
	ground_x = 100
	ground_y = 80
	score = 0

	# sets the goal positons
	def __init__(self):
		x = int(self.ground_x / 2)
		y = int(self.ground_y / 2)
		self.newBall(x, y)
		self.Goal_y1 = self.ground_y * 0.4
		self.Goal_y2 = self.ground_y * 0.6

	# resets the ball's position after goal or out of bounds
	def resetBall(self):
		x = int(self.ground_x / 2)
		y = int(self.ground_y / 2)
		self.newBall(x, y)
		self.show_score()

	# changes the ball's position and checks for goal or out of bounds
	def kick(self, x, y):
		self.ball_move(x, y)
		# checks for goal
		if self.x_pos >= self.ground_x and self.y_pos >= self.Goal_y1 and self.y_pos <= self.Goal_y2:
			print('Goal!!!')
			self.score += 1
			self.resetBall()	
		# checks for opponent's goal
		elif self.x_pos <= 0 and self.y_pos >= self.Goal_y1 and self.y_pos <= self.Goal_y2:
			print('You hit the opponent\'s goal!')
			self.score -= 1
			self.resetBall()
		# checks for out of bounds
		elif self.x_pos >= self.ground_x or self.y_pos >= self.ground_y or self.x_pos < 0 or self.y_pos <0:
			print('Ball is out of bounds!')
			self.score -= 1
			self.resetBall()

	# prints the current score
	def show_score(self):
		print('Score is', self.score)

	# prints the grounds coordinates
	def show_ground(self):
		print('Ground X coordinates are from 0 to', self.ground_x)
		print('Ground Y coordinates are from 0 to', self.ground_y)

	# prints the goal coordinates
	def show_goals(self):
		print('Your goal coordinates are >', self.ground_x,  ',', self.Goal_y1, ',', self.Goal_y2)
		print('Your opponent\'s goal coordinates are < 0', ',', self.Goal_y1, ',', self.Goal_y2)


print('\tWelcome to Football Game\n')
play = True
while play == True:
	loop = 0
	game = MyFavGame()
	game.show_ground()
	game.give_ball_pos()
	game.show_goals()
	while loop < 5:
		print('\nyou have', 5 - loop, 'move(s) left')
		choice = int(input('1. Kick the ball\n2. Check ball\'s position\n3. Check Score\n4. Check Ground coordinates \n5. Check Goal Posts\n6. Exit\n'))
		if choice == 1:
			x = int(input('Give delta x = '))
			y = int(input('Give delta y = '))
			game.kick(x, y)
			game.give_ball_pos()
			loop += 1
		elif choice == 2:
			game.give_ball_pos()
		elif choice == 3:
			game.show_score()
		elif choice == 4:
			game.show_ground()
		elif choice == 5:
			game.show_goals()
		else:
			loop = 5

	print('\nGame Over\nYou have scored', game.score, 'points')
	choice = input('Do you want to continue playing (y/n) : ')
	if choice != 'y':
		play = False
print('Thank you for playing')
