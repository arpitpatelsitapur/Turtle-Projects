import turtle as t
t.pen(speed=0)
colorlist=['red', 'purple', 'yellow', 'green', 'orange', 'blue']
i=0
t.bgcolor("black")
while i<200:
    t.color(colorlist[i%6])
    t.fd(i)
    t.lt(59)
    i+=1
t.done()