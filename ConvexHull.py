import math



#Miten vektori data esitetään?

def ConvexHull2D(Vectors):
    # Ratkaistaan kaikkein vasemmanpuolisin vektori
    pienin = Vectors[0]
    for i in range (len (Vectors)):
        if Vectors[i][0] < pienin [0]:
            pienin = Vectors[i]
    print(pienin) #Kaikkein vasemman puoleisin.

    result = [pienin]
    kulmaHolder = 0

    while True:
        SmallestAngle = math.pi * 2
        SmallestIndex = -1
        

        for i in range(len(Vectors)):
            if Vectors[i] != result[-1]: #Ei verrata itseen
                Angle = math.atan2(Vectors[i][0] - result [-1][0], Vectors[i][1]- result[-1][1] )
                if Angle < kulmaHolder:
                    Angle += 2 * math.pi
                
                print(Vectors[i], Angle)
                #Pienempi löytyi
                if Angle < SmallestAngle:
                    SmallestAngle = Angle
                    SmallestIndex = i
        if Vectors[SmallestIndex] in result: #Pyörähti ympäri
            break 
        kulmaHolder = SmallestAngle
        result.append(Vectors[SmallestIndex])
    return result

   
if __name__ == "__main__":
    # Miten vektori data esitetään?
    # x y x y
    L = [[0,0], [1,0], [0,1], [-1,0], [0,-1]]
    print(ConvexHull2D(L))