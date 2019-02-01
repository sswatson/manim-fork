
from big_ol_pile_of_manim_imports import *

class Indications(Scene):
    def construct(self):
        title = TextMobject("Animations")
        title.to_edge(UP)
        focus_on = TextMobject("FocusOn")
        focus_on.next_to(title,DOWN)
        indicate = TextMobject("Indicate")
        indicate.next_to(title,DOWN)
        apply_wave = TextMobject("ApplyWave")
        apply_wave.next_to(title,DOWN)
        wiggle_out_then_in = TextMobject("WiggleOutThenIn")
        wiggle_out_then_in.next_to(title,DOWN)

        square = Square(color=BLACK)
        
        self.play(ShowCreation(square))
        self.play(Write(focus_on))
        self.play(FocusOn(square))
        self.play(FadeOut(focus_on))
        
        self.play(Write(indicate))
        self.play(Indicate(square))
        self.play(FadeOut(indicate))

        self.play(Write(apply_wave))
        self.play(ApplyWave(square))
        self.play(FadeOut(apply_wave))

        self.play(Write(wiggle_out_then_in))
        self.play(WiggleOutThenIn(square))
        self.play(FadeOut(wiggle_out_then_in))

class Transformations(Scene):
    def construct(self):
        square = Square(color=BLACK)

        self.add(square)
#        self.play(ShowCreation(square))
        self.play(ApplyPointwiseFunction(lambda x: np.array([x[0],2*x[1],x[2]]), square))
        self.play(Rotate(square,angle=np.pi/4))

class Animations(Scene):
    def construct(self):
        title = TextMobject("Animations")
        title.to_edge(UP)
        write = TextMobject("Write")
        fade_out = TextMobject("FadeOut")
        transform = TextMobject("Transform")
        grow_from_center = TextMobject("GrowFromCenter")
        show_creation = TextMobject("ShowCreation")
        uncreate = TextMobject("Uncreate")
        fade_in = TextMobject("FadeIn")
        fade_in_from_large = TextMobject("FadeInFromLarge")
        fade_out_and_shift = TextMobject("FadeOutAndShift")
        spin_in_from_nothing = TextMobject("SpinInFromNothing")
        arrow = Arrow(LEFT,UP)
        grow_arrow = TextMobject("GrowArrow")
        arrow.next_to(grow_arrow)

        self.play(Write(title))
        self.play(Write(write))
        self.play(Transform(write,transform))
        self.play(Transform(write,fade_out))
        self.play(FadeOut(write))
        self.play(GrowFromCenter(grow_from_center))
        self.play(FadeOut(grow_from_center))
        self.play(ShowCreation(show_creation))
        self.play(Transform(show_creation,uncreate))
        self.play(Uncreate(show_creation))
        self.play(FadeIn(fade_in))
        self.play(Transform(fade_in,fade_out_and_shift))
        self.play(FadeOutAndShift(fade_in))
        self.play(SpinInFromNothing(spin_in_from_nothing))
        self.wait()
        self.remove(spin_in_from_nothing)
        self.play(FadeInFromLarge(fade_in_from_large))
        self.wait()
        self.remove(fade_in_from_large)
        self.add(grow_arrow)
        self.play(GrowArrow(arrow))


