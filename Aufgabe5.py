# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 10:48:02 2022

@author: Admin
"""
import matplotlib.pyplot as plt
import numpy as np

"""Initial values"""
R0 = 400    #initial rabbit population
C0 = 50     #initial cat population
T = 1000     #number of timesteps

"""Arrays for storing values"""
rabbitPop = [0] * T
rabbitPop[0] = R0
catPop = [0] * T
catPop[0] = C0
carKillsCats = [0] * T
carKillsRabbits = [0] * T
catKills = [0] * T

"""Working variables"""
currentTimestep = 1
eatenRabbits = 0
carRabbits = 0
carCats = 0

print("Timestep 0")
print("Environment initialized")
print(f"Rabbit population = {R0}")
print(f"Cat population = {C0}")

while currentTimestep < T:
    print("__________________")
    print(f"Timestep {currentTimestep}")
    
    """1) Rabbit population increases in the beginning of the timestep"""
    rabbitPop[currentTimestep] = rabbitPop[currentTimestep-1] * 1.1
    print(f"Rabbit population after reproduction = {rabbitPop[currentTimestep]}")

    """2) Cats hunt rabbits and rabbit population decreases"""
    eatenRabbits = (rabbitPop[currentTimestep] 
                    * 0.0005 * catPop[currentTimestep-1])
    rabbitPop[currentTimestep] = rabbitPop[currentTimestep] - eatenRabbits
    catKills[currentTimestep] = catKills[currentTimestep-1] + eatenRabbits
    print(f"Rabbits eaten this timestep {eatenRabbits}")
    
    """3) Cat population increases based on number of eaten rabbits"""
    catPop[currentTimestep] = eatenRabbits * 0.1 + catPop[currentTimestep-1]
    print(f"Rabbit population after cats hunt = {rabbitPop[currentTimestep]}")
    print(f"Cat population after reproduction = {catPop[currentTimestep]}")
    
    """4) Reduction of both populations by cars"""
    carRabbits = rabbitPop[currentTimestep] * 0.05
    carCats = catPop[currentTimestep] * 0.05
    carKillsRabbits[currentTimestep] = ((carKillsRabbits)[currentTimestep-1] 
                                        + carRabbits)
    carKillsCats[currentTimestep] = carKillsCats[currentTimestep-1] + carCats
    rabbitPop[currentTimestep] = round(rabbitPop[currentTimestep] - carRabbits)
    catPop[currentTimestep] = round(catPop[currentTimestep] - carCats)
    print(f"Rabbits killed by cars = {carKillsRabbits[currentTimestep]-carKillsRabbits[currentTimestep-1]}")
    print(f"Cats killed by cars = {carKillsCats[currentTimestep]-carKillsCats[currentTimestep-1]}")
    print(f"Final rabbit population = {rabbitPop[currentTimestep]}")
    print(f"Final cat population = {catPop[currentTimestep]}")
    
    """5) Moving onto the next timestep"""
    currentTimestep += 1

"""Plot of populations"""
x = np.arange(0, T, 1)
plt.plot(x, rabbitPop, label="Rabbit Population", color="royalblue")
plt.plot(x, catPop, label="Cat Population", color="darkorange")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Rabbit and cat population in time")
plt.grid()
plt.legend(ncol=1)
plt.show()

"""Plot of animals killed by cars"""
x = np.arange(0, T, 1)
plt.plot(x, carKillsRabbits, label="Rabbits killed by cars", color="red")
plt.plot(x, catKills, label="Rabbits killed by cats", color="orange")
plt.plot(x, carKillsCats, label="Cats killed by cars", color="black")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Total ammount of animals ran over by car")
plt.grid()
plt.legend(ncol=1)
plt.show()