size(800,600)
background(0)
fill(255)
stroke(102)
for y in range(20, height-15,20):
    for x in range(20, width-15,20):
        ellipse(x,y,4,4)
        line(x,y,240,60)
