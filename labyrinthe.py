taille = 200
longLiHori = 10
clear(taille*1.5, taille*1.5)

def liHoriColo(posVert,c):
    SautAleat = 0 #longueur aleatoire
    posY = taille
    while posY > 0:
        pu()
        goto(-taille/2 + posVert, taille/2 - posY)
        pd()
        fd(taille/longLiHori)
        rt(90)
        fd(taille/longLiHori*2)
        SautAleat = c*int(4*random())+20
        posY = posY - SautAleat
        
        
def liVertiColo(posVert,c):
    SautAleat = 0 #longueur aleatoire
    posX = taille
    while posX > 0:
        pu()
        goto(taille/2 - posX, -taille/2 + posVert)
        pd()
        fd(taille/longLiHori)
        rt(90)
        fd(taille/longLiHori*2)
        SautAleat = c*int(4*random())+20
        posX = posX - SautAleat

def mulLiHoriColo(horiOuVerti,c): 
    nbSautVert = taille/longLiHori
    coef = nbSautVert/10
    for x in range(0, int(nbSautVert/2)):
        horiOuVerti(coef*x*longLiHori,c)
def trouMilieu():
    pu()
    goto(7,0)
    pensize(4)
    pencolor(1,0,1)
    pd()
    fd(4)
    bk(5)
    ht()
    
        
def globallaby():

    mulLiHoriColo(liHoriColo,40)
    rt(90)
    mulLiHoriColo(liVertiColo,80)
    rt(90)
    mulLiHoriColo(liHoriColo,40)
    trouMilieu()
    
    
globallaby()
