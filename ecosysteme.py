
from numpy.random import randint

class Ecosystem(list):
    def __init__(self,nbvehic,nbturn,maxlength,maxwidth=4):

        self.nbvehic=nbvehic
        self.nbturn=nbturn
        self.maxlength=maxlength
        self.maxwidth=maxwidth



    def __str__(self):
        """
        remodel the str function to show our road
        :return:
        """
        return self.str2()

    def str2(self):
        """
        function to create our endless road
        :return:
        """
        r=""
        for i in range (self.maxwidth+1):
            for j in range (self.maxlength+1):
                r+="."
            r+="\n"
            return r



    def placement(self):
        """
        places the vehicles on the road
        :return:
        """
        x=randint(0,self.maxwidth)
        y=randint(0,self.maxlength)
        return (x,y)


    def turn(self):
        """
        creates intends in which our vehicles will move
        :return:
        """
        pass

    def simlulate(self):
        """
        simulation of a turn
        :return:
        """
        pass


if __name__ == "__main__":
    e=Ecosystem(3,3,100,2)

    print(e)