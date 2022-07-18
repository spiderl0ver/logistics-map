from graphics import *
win = GraphWin("run", 600,600)
newwin = GraphWin("Hello",600,600)
newwin.setCoords(0,0,4,1)
#xn+1 = rx(1-x)
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def generateequ(x,r,tsample):
    xvalues = []
    xvalues.append(r*x*(1-x))
    for i in range(tsample):
        xappend = r*xvalues[i] * (1-xvalues[i])
        xvalues.append(xappend)
    return xvalues
for t in range(50):
    for r in range(40):
        r = (r+(t/50))/10
        for x in range(10):
            x = x/10
            clear(win)
            points = generateequ(x,r,200)
            win.setCoords(-1,min(points)-0.0001,20+1,max(points)+0.0001)
            for i in range(0,20):
                line = Line(Point(i,points[i]),Point(i+1,points[i+1]))
                line.draw(win)
            for g in range(195,200):
                newwin.plot(r,points[g],"black")





win.getKey()
win.close()
