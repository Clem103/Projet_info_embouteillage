from numpy import ones
from random import randint



class Ecosystem(list):
    def __init__(self,nbturn,maxlength,maxwidth=4,nbvehic=0):

        self.nbvehic=nbvehic
        self.nbturn=nbturn
        self.maxlength=maxlength
        self.maxwidth=maxwidth
        if self.nbvehic>=self.maxlength*self.maxwidth:
            raise (ValueError("Too many vehicles"))

        self.coord = self.placementinitial()

    def __str__(self):
        return self.str2()


    def placementinitial(self):
        """
        places the vehicles on the road
        :return:
        """

        coordinit=ones((self.maxwidth,self.maxlength))

        trucknb=int(self.nbvehic*1/3)
        carnb=self.nbvehic-trucknb


        for i in range (carnb):
            x=randint(0,self.maxwidth-1)
            y=randint(0,self.maxlength-1)
            while coordinit[x][y]==2 or coordinit[x][y]==0:
                x = randint(0, self.maxwidth - 1)
                y = randint(0, self.maxlength - 1)
            coordinit[x][y]=0

        for j in range (trucknb):
            x=randint(self.maxwidth-2,self.maxwidth-1)
            y=randint(0,self.maxlength-1)
            while coordinit[x][y]==2 or coordinit[x][y]==0:
                x = randint(self.maxwidth - 2, self.maxwidth - 1)
                y = randint(0, self.maxlength - 1)
            coordinit[x][y]=2

# soucis avec les randint: il peut sortir une paire de coordonnées égales, on aura dans ce cas 1 voiture en moins.
        for j in range(self.maxwidth):
            for k in range(self.maxlength-2):
                #permet de vérifier l'espacement entre deux véhicule au début de la simulation
                if coordinit[j][k+1]==0 and coordinit[j][k]==0:
                    coordinit[j][k+1]=1
                    coordinit[j][k+2]=0
                if coordinit[j][k+1]==2 and coordinit[j][k]==2:
                    coordinit[j][k+1]=1
                    coordinit[j][k+2]=2
                if coordinit[j][k+1]==0 and coordinit[j][k]==2:
                    coordinit[j][k+1]=1
                    coordinit[j][k+2]=0
                if coordinit[j][k+1]==2 and coordinit[j][k]==0:
                    coordinit[j][k+1]=1
                    coordinit[j][k+2]=2

        return coordinit

    def str2(self):
        """
        function to print our endless road
        :return:
        """
        r=""
        #coord=Ecosystem.placementinitial(self)

        for i in range (self.maxwidth):
            for j in range (self.maxlength):
                if self.coord[i][j]==0:
                    r+="_CAR_"
                elif self.coord[i][j]==2:
                    r+="TRUCK"
                else:
                    r+="_____"
            r+="\n"

        return r


    def turn(self):
        """
        creates a turn in which our vehicles will move
        :return:
        """
        coord=Ecosystem.placementinitial(self)

        pass


    def simlulate(self):
        """
        simulation of a turn
        :return:
        """
        pass
        for i in range(self.nbturn):
            print("TURN N°",i)
            Ecosystem.turn(self)


if __name__ == "__main__":
    e=Ecosystem(0,70,4,100)
    print(e)