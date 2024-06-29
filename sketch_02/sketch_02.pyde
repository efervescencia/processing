

def setup():
    size(800,600)
    background(255)  # Limpia el lienzo con un fondo blanco
    stroke(0)  # Establece el color de los puntos a negro
    point(240,60)
    
    point(1,1)
    point(799,599)
    point(799,1)
    point(1,599)
    
    for x in range(0, 800):
        point(x, 300)
        
    for y in range(0, 600):
        point(400, y)
        
    for x in range(800):  # diagonal trazada con puntos
        y=x*600/800
        point(x,y)

    line (200,200,600,600)
    
    triangle(400,400,500,500,350,450)
    quad(100,100,100,200,300,200,300,100)
    rect(500,500,50,50)
    ellipse(300,50,40,60)
    arc(300,300,50,60,0,HALF_PI)
    arc(300,300,50,60,radians(120),radians(140))
    
