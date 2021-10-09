import math
import numpy as np
import matplotlib.pyplot as plt

satellites = np.array([])

class Object():
    def __init__(self, position, x_velocity, y_velocity, hasGravity, mass, satellites):
        self.pos = position
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.hasGravity = hasGravity
        self.mass = mass

        self.acceleration = updateAcceleration(satellites)

    def updateAcceleration(self, satellites):
        xres = 0
        yres = 0
        for satellite in satellites:
            
            if satellite.hasGravity:
                separation = math.sqrt((position[0]-satellite.pos[0])**2+
                                      (position[1]-satellite.pos[1])**2)

                g = 6.67e-11*satellite.mass/separation**2

                direction = [satellite.pos[0]-position[0],satellite.pos[1]-position[1]]
                T = math.sqrt(sum([x**2 for x in direction]))
                normalised = [x/T for x in direction]

                xres += normalised[0]*g
                yres += normalised[1]*g

        self.acceleration = [xres, yres]

xdata = [satellite.pos[0] for satellite in satellites]
ydata = [satellite.pos[1] for satellite in satellites]

plot, = plt.plot([], [])
plt.set_xdata
plt.draw()
