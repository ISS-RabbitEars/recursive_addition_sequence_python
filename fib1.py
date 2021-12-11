import math
import matplotlib.pyplot as plt
from matplotlib import animation

class vec:
	def __init__(self,a,b):
		self.x=a
		self.y=b
	def mag(self):
		return math.sqrt(self.x**2+self.y**2)
	def hat(self):
		return vec(self.x/self.mag(), self.y/self.mag())
	def dot(self,r1):
		return self.x*r1.x+self.y*r1.y
	def add(self,r1):
		return vec(self.x+r1.x, self.y+r1.y)
	def __add__(self,r1):
		return self.add(r1)
	def sub(self,r1):
		return vec(self.x-r1.x, self.y-r1.y)
	def __sub__(self,r1):
		return self.sub(r1)
	def mul(self,a):
		return vec(a*self.x, a*self.y)
	def __mul__(self,a):
		return self.mul(a)
	def __rmul__(self,a):
		return self*a
	def div(self,a):
		return vec(self.x/a, self.y/a)
	def rot(self,a):
		return vec(self.x*math.cos(a)+self.y*math.sin(a), -self.x*math.sin(a)+self.y*math.cos(a))
	def __iadd__(self,r1):
		return self+r1
	def __isub__(self,r1):
		return self-r1


def setplot1(sx,sy):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-sx,sx])
	plt.ylim([-sy,sy])
	ax.set_facecolor('xkcd:black')

def setplot2(sx1,sx2,sy1,sy2):
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([sx1,sx2])
	plt.ylim([sy1,sy2])
	ax.set_facecolor('xkcd:black')

frps=30
sec=5
nx=36
fs=frps*sec
x=[]
y=[]
dt1=math.pi/fs
dt=dt1/2
dx=1/fs
p=1.5
fig, a=plt.subplots()

#for a fibonacci spiral set fa=0
fa=10
fb=fa+1
c=vec(0,0)
fas=fa
def run(frame):
	global fa,fb,c
	if (frame!=0 and frame%fs==0):
		temp=fb
		fb+=fa
		fa=temp
	plt.clf()
	x.append(c.x+fb*math.cos(frame*dt-math.pi/2))
	y.append(c.y+fb*math.sin(frame*dt-math.pi/2))
	plt.plot(x,y,color='r')
	if (frame!=0 and frame%fs==fs-1):
		xf=vec(x[frame],y[frame])
		dr=xf-c
		drh=-fa*dr.hat()
		c+=drh
	xmax=max(x)
	if(xmax<1):
		xmax=1
	xmin=min(x)
	ymax=max(y)
	if(ymax<0):
		ymax=0
	ymin=min(y)
	setplot2(p*xmin,p*xmax,p*ymin,p*ymax)
	#plt.title('Fibonacci Spiral')
	plt.suptitle('Recursive Addition Sequence')
	plt.title('seed = '+str(fas))

ani=animation.FuncAnimation(fig,run,interval=1,frames=nx*fs)
writervideo = animation.FFMpegWriter(fps=frps)
ani.save('ras.mp4', writer=writervideo)
plt.show()

