"""
Program 1
Title: Travel Game
Description: 
	You commute on a road and play a game
	1. Start the count as 0
	2. Add 1 for every car that you overtake
	3. Subtract 1 for every car that overtakes you
	4. Stop counting when you reach your destination

	Write a function “MyTravel_MyGame” which takes in
	· The total distance (in m)
	· How fast you are going (mps)
	· Information about other cars
	· Their time (relative to you) as you join the road
	· For example,
		· -1.5 means they already passed your starting point 1.5 minutes ago
		· 2.0 means they will pass your starting point 2.0 minutes from now
	· How fast the other car is traveling (mps)
Author: akashroshan135
Date: 04-Feb-2021
"""

def MyTravel_MyGame(distance, myMPS, relativeTime, carMPS):
	carDistanceTravelled = ((int(relativeTime) * 60) + ((relativeTime - int(relativeTime)) * 60)) * -1 * carMPS
	carDistanceTravelled += carMPS * (distance / myMPS)
	if distance > carDistanceTravelled:
		return 1
	return 0


carsUserPassed = 0
carsPassedUser = 0
carTime = []
carMPs = []

distance = int(input("Enter the total distance: "))
myMPS = int(input("Enter your speed (mps):  "))
carNo = int(input("Enter the number of cars: "))

for i in range(carNo):
	carTime.append(float(input("Enter the car " + str(i + 1) + "'s time relative to you (in mins): ")))
	carMPs.append(int(input("Enter the car " + str(i + 1) + "'s speed (mps):  ")))
	if MyTravel_MyGame(distance, myMPS, carTime[i], carMPs[i]):
		carsUserPassed += 1
	else:
		carsPassedUser += 1
	
print("The total number of cars you passed is", carsUserPassed)
print("The total number of cars that passed you is", carsPassedUser)
