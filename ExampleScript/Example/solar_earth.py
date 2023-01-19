
import vpython as vp
import numpy as np


# sun data
sunsize = 696342.0

# plantary data
orbit = 365.3
size = 6378
rad = 149600000

# plot parameters
framerate = 10
tscale = 30
sizescale = 50
radscale = 1.0/20

graph1=vp.canvas(width=800, height=1000,background=vp.color.white)

# create the sun
vp.sphere(pos=vp.vector(0,0,0), radius=sunsize, color=vp.color.yellow)

# create the planet
x = radscale*rad
y = 0.0
planet = vp.sphere(pos=vp.vector(x,y,0), radius=sizescale*size, color=vp.color.blue, make_trail=False)

# begin time
t = 0.0
counter=0
while True:
    vp.rate(framerate) 
    t += tscale/framerate

# move planets in their orbits
    x = radscale*rad*np.cos(2*np.pi*t/orbit)
    y = radscale*rad*np.sin(2*np.pi*t/orbit)
    planet.pos = vp.vector(x, y, 0)

    counter+=1
    #graph1.capture('test_'+str(counter))
