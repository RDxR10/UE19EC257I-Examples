import numpy as np
import matplotlib.pyplot as pl


t0=-100.
dt=0.001
t=np.arange(t0,-t0,dt)

f=1./(t**2+1.)


g=np.fft.fft(f)
w = np.fft.fftfreq(f.size)*2*np.pi/dt
g*=dt*np.exp(-complex(0,1)*w*t0)/(np.sqrt(2*np.pi))
pl.scatter(w,g,color="r")
pl.plot(w,np.exp(-np.abs(w))*np.sqrt(np.pi/2),color="g")

pl.gca().set_xlim(-10,10)
pl.show()
pl.close()
