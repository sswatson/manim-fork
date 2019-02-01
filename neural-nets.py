

from big_ol_pile_of_manim_imports import *

weights = [np.matrix([[1,2],[3,4],[5,2]]),
           np.matrix([[-1,3],[0,5]])]

W_mobj = [matrix_to_mobject(W) for W in weights] 

biases = [np.array([-5,2,5]),np.array([0,4])]

b_mobj = [matrix_to_mobject(b) for b in biases] 

x = matrix_to_mobject(np.array([-4,2]))

plus = TexMobject("+")
equals = TexMobject("=")

class ForwardProp(Scene):

    def construct(self):
        x.next_to(W_mobj[0])
        plus.next_to(x)
        b_mobj[1].next_to(plus)
        equals.next_to(b_mobj[1])
        for m in [W_mobj[0],x,plus,b_mobj[1],equals]: 
            self.play(Write(m))
