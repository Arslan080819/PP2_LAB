class Ball:
    def __init__(self,x,y,radius,w,h):
        self.x=x
        self.y=y
        self.radius=radius
        self.w=w
        self.h=h

    def move(self,dx,dy):
        nx=self.x+dx
        ny=self.y+dy

        if self.radius <= nx <= self.w-self.radius:
            self.x=nx
        if self.radius <= ny <= self.h-self.radius:
            self.y=ny
