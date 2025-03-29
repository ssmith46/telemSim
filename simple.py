#For most of the array based stuff
import numpy as np

#For the visulations of graphs
import matplotlib.pyplot as plt


###########Keplars Laws of Motion###############
#As taken from Nasa's website: https://science.nasa.gov/resource/orbits-and-keplers-laws/

###	Kepler's First Law: each planet's orbit about the Sun is an ellipse. 
###						The Sun's center is always located at one focus of the orbital ellipse. 
###						The Sun is at one focus. The planet follows the ellipse in its orbit, meaning 
###						that the planet to Sun distance is constantly changing as the planet goes around its orbit.
###
### Kepler's Second Law: the imaginary line joining a planet and the Sun sweeps equal areas of space during 
###						 equal time intervals as the planet orbits. Basically, that planets do not move with 
###						 constant speed along their orbits. Rather, their speed varies so that the line joining 
###						 the centers of the Sun and the planet sweeps out equal parts of an area in equal times. 
###						 The point of nearest approach of the planet to the Sun is termed perihelion. The point 
###						 of greatest separation is aphelion, hence by Kepler's Second Law, a planet is moving 
###						 fastest when it is at perihelion and slowest at aphelion.
###
### Kepler's Third Law: the squares of the orbital periods of the planets are directly proportional to the cubes 
###						of the semi-major axes of their orbits. Kepler's Third Law implies that the period for a 
###						planet to orbit the Sun increases rapidly with the radius of its orbit. Thus we find that 
###						Mercury, the innermost planet, takes only 88 days to orbit the Sun. The earth takes 365 days, 
###						while Saturn requires 10,759 days to do the same. Though Kepler hadn't known about gravitation 
###						when he came up with his three laws, they were instrumental in Isaac Newton deriving his theory 
###						of universal gravitation, which explains the unknown force behind Kepler's Third Law. Kepler and 
###						his theories were crucial in the better understanding of our solar system dynamics and as a 
###						springboard to newer theories that more accurately approximate our planetary orbits.
###
### Takeaways: The "round-ness" of the orbit of our satellite is called 'Eccentricity', where:
###						- 0 = Perfect Circle
###						- 1 = Will never be one, but can get close
###			   Satellites can have a wide range of eccentricity values for their orbits, ranging from near circular
###			   to extremely extremely elliptical (called Molniya orbits). Our simulation will acconut for these types
###			   of orbits. 
###	
###			   Because the speed of satellites are not the same during orbit, our simulation should differentiate the
###			   speed of the satellite during its orbit in the usage of colors on the graph. We will represent this 
###			   with color values of:
###			   		    - Blue = perihelion (fastest speed during orbit)
###					    - Red  = aphelion (slowest speed during orbit)
###			   This will allow for visual representation of the orbit speeds as our satellite orbits earth.
###
###			   Our simulation will calculate the time in which it takes our satellite to orbit around the earth, and 
###			   because of Keplar's third law, we can expect for increased orbit times, the larger the radius of orbit
###			   for our satellite is. The full length of time it takes for our satellite to make one orbit around the Earth
###			   will be displayed on the graph.

### Newton's Law of Universal Gravitation: Basically the force that two entities extert on each other in terms of gravitational
###										   pull can be solved using the following equation:
###
###										   		Fg = G * ((m1 * m2) / r^2)
###													
###													Fg = Gravitational Force
###													G = Universal Gravitational Constant (6.6743 × 10-11 m^3 kg^-1 s^-2)
###													m1 = mass of object 1
###													m2 = mass of object 2
###													r = seperation between the two objects
###										   
###										 This equation will be used to calculate the forces that our satellite and Earth inclict
###									     on each other.


###Attributes of our satellite (imitating Starlink stats from following website:
###		https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=2019-074D#:~:text=The%20Starlink%20satellites%20feature%20a,use%20krypton%2Dfueled%20Hall%20thrusters.
### These are magic numbers for the equation, thus they are located at the top for easier changeability
SAT_MASS = 260 #kilograms
ORBIT_RADIUS = 550 #kilometers


### Values taken from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
EARTH_RADIUS = 6378.137 #kilometers
EARTH_MASS = 5.9722e24 #kilograms
UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.6743e-11 #m^3 kg^-1 s^-2

