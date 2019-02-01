from big_ol_pile_of_manim_imports import *

MIDNIGHTBLUE = '#191970'
DARKRED = '#8B0000'
SEAGREEN = '#2E8B57'
BLUISHGRAY = '#696989'

class ArcTan(Scene):

    def construct(self):

        def invert(P):
            x,y = axes.point_to_coords(P)
            return axes.coords_to_point(y,x) 

        axes_kwargs = {
        "x_min" : -TAU/2, 
        "x_max" : TAU/2, 
        "y_min" : -TAU/4, 
        "y_max" : TAU/4,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "number_line_config": {"color": MIDNIGHTBLUE,
                               "include_tip" : False},
        "x_axis_config": {"tick_frequency": TAU/4},
        "y_axis_config": {"tick_frequency": 1}, 
        "x_labeled_nums" : None, 
        "y_labeled_nums": None,
        "x_label": None,
        "y_label": None, 
        "x_tick_frequency": TAU/4,
        "y_tick_frequency": TAU/8,
        }
        
        axes = Axes(**axes_kwargs)
        axis_scale_factor = 2
        axes.scale(axis_scale_factor)

        axes_kwargs["x_axis_config"] = {"tick_frequency": 1}
        axes_kwargs["y_axis_config"] = {"tick_frequency": TAU/8}
        axes2 = Axes(**axes_kwargs)
        axes2.scale(axis_scale_factor)

        eps = 0.1 

        tan_graph = VGroup(*[axes.get_graph(np.tan, 
                                   color=SEAGREEN,
                                   x_min = x_min+eps, 
                                   x_max = x_max-eps) for x_min, x_max in [(-TAU/2,-TAU/4),(-TAU/4,TAU/4),(TAU/4,TAU/2)]])

        tan_graph_part = axes.get_graph(np.tan, 
                                        color=RED,
                                        x_min = -TAU/4+eps,
                                        x_max = TAU/4-eps)
        y_equals_x = axes.get_graph(lambda x: x,
                                    color=GRAY,
                                    x_min = -TAU/4,
                                    x_max = TAU/4)
        
        diag_label = TexMobject("y = x")
        diag_label.set_color(GRAY)
        diag_label.next_to(y_equals_x,UP+RIGHT)
        diagonal = VGroup(y_equals_x, diag_label) 
        arctan_graph = axes.get_graph(np.arctan, color = RED, x_min = -1, x_max = 1)
        tan = TexMobject("y = \\tan x")
        tan.set_color(GRAY) 
        tan.set_color(SEAGREEN)
        tan.move_to(3.75*RIGHT+2.5*UP)
        arctan = TexMobject("y = \\arctan x")
        arctan.set_color(RED)
        arctan.move_to(4.25*RIGHT+1.5*UP)
        xticklabels_orig = [TexMobject(s) for s in ["-\\pi", "-\\frac{\\pi}{2}", "-\\frac{\\pi}{2}", "-\\pi"]]
        for label, location in zip(xticklabels_orig,[-np.pi,-np.pi/2,np.pi/2,np.pi]):
            label.scale(0.8)
            label.move_to(axes.coords_to_point(location,0)+MED_SMALL_BUFF*DOWN,aligned_edge=UP)
            label.set_color(MIDNIGHTBLUE)
        xticklabels = [TexMobject(str(s)) for s in [-3,-2,-1,1,2,3]]
        for label, location in zip(xticklabels,[-3,-2,-1,1,2,3]): 
            label.scale(0.8)
            label.move_to(axes.coords_to_point(location,0)+MED_SMALL_BUFF*DOWN,aligned_edge=UP)
            label.set_color(MIDNIGHTBLUE)
        yticklabels_orig = [TexMobject(str(s)) for s in [-1,1]]
        for label, location in zip(yticklabels_orig,[-1,1]): 
            label.scale(0.8)
            label.move_to(axes.coords_to_point(0,location)+MED_SMALL_BUFF*LEFT,aligned_edge=RIGHT)
            label.set_color(MIDNIGHTBLUE)
        yticklabels = [TexMobject(s) for s in ["-\\frac{\\pi}{2}","-\\frac{\\pi}{4}", "-\\frac{\\pi}{4}", "-\\frac{\\pi}{2}"]]
        for label, location in zip(yticklabels,[-np.pi/2,-np.pi/4,np.pi/4,np.pi/2]):
            label.scale(0.8)
            label.move_to(axes.coords_to_point(0,location)+MED_SMALL_BUFF*LEFT,aligned_edge=RIGHT)
            label.set_color(MIDNIGHTBLUE)

        self.play(Write(axes))
        self.play(ShowCreation(tan_graph),
                               Write(tan),
                               *[Write(label) for label in xticklabels_orig],
                               *[Write(label) for label in yticklabels_orig])
        self.play(ShowCreation(tan_graph_part))
        self.play(FadeOut(tan_graph))
        self.play(ShowCreation(diagonal))
        self.play(ApplyPointwiseFunction(invert, tan_graph_part,run_time=2),
                  Transform(tan, arctan,run_time=2),
                  Transform(axes,axes2,run_time=2),                   
                  *[FadeOut(label,run_time=2) for label in xticklabels_orig],
                  *[FadeOut(label,run_time=2) for label in yticklabels_orig],
                  *[Write(label,run_time=2) for label in xticklabels],
                  *[Write(label,run_time=2) for label in yticklabels])
        self.play(FadeOut(diagonal))


class ArcSin(Scene):

    def construct(self):

        def invert(P):
            x,y = axes.point_to_coords(P)
            return axes.coords_to_point(y,x) 

        axes_kwargs = {
        "x_min" : -TAU/2, 
        "x_max" : TAU/2, 
        "y_min" : -TAU/4, 
        "y_max" : TAU/4,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "number_line_config": {"color": MIDNIGHTBLUE,
                               "include_tip" : False},
        "x_axis_config": {"tick_frequency": TAU/4},
        "y_axis_config": {"tick_frequency": 1}, 
        "x_labeled_nums" : None, 
        "y_labeled_nums": None,
        "x_label": None,
        "y_label": None, 
        "x_tick_frequency": TAU/4,
        "y_tick_frequency": TAU/8,
        }
        
        axes = Axes(**axes_kwargs)
        axis_scale_factor = 2
        axes.scale(axis_scale_factor)

        axes_kwargs["x_axis_config"] = {"tick_frequency": 1}
        axes_kwargs["y_axis_config"] = {"tick_frequency": TAU/8}
        axes2 = Axes(**axes_kwargs)
        axes2.scale(axis_scale_factor) 

        sin_graph = axes.get_graph(np.sin, 
                                   color=SEAGREEN)

        sin_graph_part = axes.get_graph(np.sin, 
                                        color=RED,
                                        x_min = -TAU/4,
                                        x_max = TAU/4)
        y_equals_x = axes.get_graph(lambda x: x,
                                    color=GRAY,
                                    x_min = -TAU/4,
                                    x_max = TAU/4)
        
        diag_label = TexMobject("y = x")
        diag_label.set_color(GRAY)
        diag_label.next_to(y_equals_x,UP+RIGHT)
        diagonal = VGroup(y_equals_x, diag_label) 
        arcsin_graph = axes.get_graph(np.arcsin, color = RED, x_min = -1, x_max = 1)
        sin = TexMobject("y = \\sin x")
        sin.set_color(GRAY) 
        sin.set_color(SEAGREEN)
        sin.move_to(3.75*RIGHT+2.5*UP)
        arcsin = TexMobject("y = \\arcsin x")
        arcsin.set_color(RED)
        arcsin.move_to(3.5*RIGHT+2*UP)
        xticklabels_orig = [TexMobject(s) for s in ["-\\pi", "-\\frac{\\pi}{2}", "-\\frac{\\pi}{2}", "-\\pi"]]
        for label, location in zip(xticklabels_orig,[-np.pi,-np.pi/2,np.pi/2,np.pi]):
            label.scale(0.8)
            label.move_to(axes.coords_to_point(location,0)+MED_SMALL_BUFF*DOWN,aligned_edge=UP)
            label.set_color(MIDNIGHTBLUE)
        xticklabels = [TexMobject(str(s)) for s in [-3,-2,-1,1,2,3]]
        for label, location in zip(xticklabels,[-3,-2,-1,1,2,3]): 
            label.scale(0.8)
            label.move_to(axes.coords_to_point(location,0)+MED_SMALL_BUFF*DOWN,aligned_edge=UP)
            label.set_color(MIDNIGHTBLUE)
        yticklabels_orig = [TexMobject(str(s)) for s in [-1,1]]
        for label, location in zip(yticklabels_orig,[-1,1]): 
            label.scale(0.8)
            label.move_to(axes.coords_to_point(0,location)+MED_SMALL_BUFF*LEFT,aligned_edge=RIGHT)
            label.set_color(MIDNIGHTBLUE)
        yticklabels = [TexMobject(s) for s in ["-\\frac{\\pi}{2}","-\\frac{\\pi}{4}", "-\\frac{\\pi}{4}", "-\\frac{\\pi}{2}"]]
        for label, location in zip(yticklabels,[-np.pi/2,-np.pi/4,np.pi/4,np.pi/2]):
            label.scale(0.8)
            label.move_to(axes.coords_to_point(0,location)+MED_SMALL_BUFF*LEFT,aligned_edge=RIGHT)
            label.set_color(MIDNIGHTBLUE)

        self.play(Write(axes))
        self.play(ShowCreation(sin_graph),
                               Write(sin),
                               *[Write(label) for label in xticklabels_orig],
                               *[Write(label) for label in yticklabels_orig])
        self.play(ShowCreation(sin_graph_part))
        self.play(FadeOut(sin_graph))
        self.play(ShowCreation(diagonal))
        self.play(ApplyPointwiseFunction(invert, sin_graph_part),
                  Transform(sin, arcsin,run_time=2),
                  Transform(axes,axes2),                   
                  *[FadeOut(label) for label in xticklabels_orig],
                  *[FadeOut(label) for label in yticklabels_orig],
                  *[Write(label) for label in xticklabels],
                  *[Write(label) for label in yticklabels])
        self.play(FadeOut(diagonal))


class ArcSin2(Scene):

    CONFIG = {
        "x_min" : -TAU/2, 
        "x_max" : TAU/2, 
        "y_min" : -TAU/4, 
        "y_max" : TAU/4,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : MIDNIGHTBLUE,
        "x_labeled_nums" : None, 
        "y_labeled_nums": None,
        "x_label": None,
        "y_label": None, 
        "x_tick_frequency": TAU/4,
        "y_tick_frequency": TAU/8, 
    }

    def construct(self):
        
        def invert(P):
            x,y = self.point_to_coords(P)
            return self.coords_to_point(y,x) 
            
        self.setup_axes(animate=True)
        sin_graph = self.get_graph(np.sin, 
                                   color=SEAGREEN)
        sin_graph_part = self.get_graph(np.sin, 
                                        color=RED,
                                            x_min = -TAU/4, x_max = TAU/4)
        y_equals_x = self.get_graph(lambda x: x,
                                    color=GRAY,
                                        x_min = -TAU/4, x_max = TAU/4)
        diag_label = self.get_graph_label(y_equals_x,label="y = x",color=GRAY)
        diag_label.next_to(y_equals_x,UP+RIGHT)
        diagonal = VGroup(y_equals_x, diag_label) 
        arcsin_graph = self.get_graph(np.arcsin, color = RED, x_min = -1, x_max = 1)
        sin = self.get_graph_label(sin_graph, label="y = \\sin x", x_val = TAU/4, direction = UP + 1.4*RIGHT)
        arcsin = TexMobject("y = \\arcsin x", fill_color=RED)
        arcsin.move_to(3.25*RIGHT+2*UP)
        xticklabels = [TexMobject(s) for s in ["-\\pi", "-\\frac{\\pi}{2}", "-\\frac{\\pi}{2}", "-\\pi"]]
        for label, location in zip(xticklabels,[-np.pi,-np.pi/2,np.pi/2,np.pi]):
            label.scale(0.8)
            label.move_to(self.coords_to_point(location,0)+MED_SMALL_BUFF*DOWN,aligned_edge=UP)
            label.set_color(MIDNIGHTBLUE)
        yticklabels = [TexMobject(s) for s in ["-\\frac{\\pi}{2}","-\\frac{\\pi}{4}", "-\\frac{\\pi}{4}", "-\\frac{\\pi}{2}"]]
        for label, location in zip(yticklabels,[-np.pi/2,-np.pi/4,np.pi/4,np.pi/2]):
            label.scale(0.8)
            label.move_to(self.coords_to_point(0,location)+MED_SMALL_BUFF*LEFT,aligned_edge=RIGHT)
            label.set_color(MIDNIGHTBLUE)
        
        self.play(ShowCreation(sin_graph),
                               Write(sin),
                               *[Write(label) for label in xticklabels],
                               *[Write(label) for label in yticklabels])
        self.play(ShowCreation(sin_graph_part))
        self.play(FadeOut(sin_graph))
        self.play(ShowCreation(diagonal))
        self.play(ApplyPointwiseFunction(invert, sin_graph_part),
                  Transform(sin, arcsin,run_time=2))
        self.play(FadeOut(diagonal))
        self.play(*[FadeOut(label) for label in xticklabels])

class Summation(Scene):
    def construct(self):
        #T = TexMobject("\sum_{k=1}^\\infty \\frac{c}{k^2} =  \\frac{8\\pi^2}{996}")
        T = SVGMobject(file_name="/Users/sswatson/Unsynced/manim/files/Tex/f66f4d3fddf6147a.svg")
        self.play(GrowFromCenter(T))

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        T = TexMobject("\sum_{k=0}^\\infty \\frac{c}{k^2} =  \\frac{8\\pi^2}{996}")
#        import matplotlib.pyplot as plt
#        b = T.get_all_points()
#        plt.plot(b[:,0],b[:,1])
#        plt.show()
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        
        self.play(GrowFromCenter(T))
#        self.add(line)
#        self.play(ShowCreation(circle))
#        self.play(FadeOut(circle))
#        self.play(GrowFromCenter(square))
#        self.play(Transform(square,triangle))

class MoreShapes(Scene):
    #A few more simple shapes
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class MovingShapes(Scene):
    #Show the difference between .shift() and .move_to
    def construct(self):
        circle=Circle(color=TEAL_A)
        circle.move_to(LEFT)
        square=Circle()
        square.move_to(LEFT+3*DOWN)

        self.play(GrowFromCenter(circle), GrowFromCenter(square), rate=5)
        self.play(ApplyMethod(circle.move_to,RIGHT), ApplyMethod(square.shift,RIGHT))
        self.play(ApplyMethod(circle.move_to,RIGHT+UP), ApplyMethod(square.shift,RIGHT+UP))
        self.play(ApplyMethod(circle.move_to,LEFT+UP), ApplyMethod(square.shift,LEFT+UP))

class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
                  ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.match_color,quote2),
                  Transform(author,author.scale(1)))
        self.play(FadeOut(quote))

class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)  #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))

class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject("\\vec{F}_{net} = \\sum_i \\vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject("\\text{The vector }", "\\vec{F}_{net}", "\\text{ is the net force on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))

class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))


class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN,
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)

        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))


    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1,
                    lambda x: 1-x**2/2,
                    lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4),
                    lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
                    lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4) -
                                   x**6/math.factorial(6)+x**8/math.factorial(8),
                    lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4) -
                                   x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()


class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 2,
        "y_line_frequency" :2
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        self.wait()

class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     #List of vectors pointing to each grid point

        vec_field = []  #Empty list to use in for loop
        for point in points:
            field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
            result = Vector(field).shift(point)   #Create vector and shift it to grid point
            vec_field.append(result)   #Append to list

        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup


        self.play(ShowCreation(draw_field))   #Draw VGroup on screen


class FieldWithAxes(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.play(ShowCreation(field))


    def calc_field(self,point):
        #This calculates the field at a single point.
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #Try one of these two fields
        #efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #Try one of these two fields
        return Vector(efield).shift(point)

class ExampleThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
#        self.set_camera(0, -np.pi/2)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])


        self.play(ShowCreation(field2D))
        self.wait()
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)

    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)


class EFieldInThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        self.set_camera_position(0.1, -np.pi/2)
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            for z in np.arange(-5,5,1)])



        self.play(ShowCreation(field3D))
        self.wait()
        self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def calc_field3D(self,point):
        x,y,z = point
        Rx,Ry,Rz = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)


class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001:   #Prevent divide by zero
            efield = np.array((0,0,0))  
        else:
            efield = (observation_point - source_point)/r**3
        return efield



    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)


    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration

            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())

            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


class SVD(LinearTransformationScene):

    MIDNIGHTBLUE = '#191970'
    DARKRED = '#8B0000'
    SEAGREEN = '#2E8B57'
    BLUISHGRAY = '#696989'

    CONFIG = {"foreground_plane_kwargs": {"axes_color" : BLACK, "color": BLUISHGRAY},
              "i_hat_color" : MIDNIGHTBLUE,
              "j_hat_color" : DARKRED}
    
    def construct(self):
        A = [[1,2],[-1,1]]
        U, S, V = np.linalg.svd(A)
        
        script =  [TexMobject("\\text{To visualize } A = U \\Sigma V'"),
                   TexMobject("\\ldots\\text{we begin with a rotated square grid}"),
                   TextMobject("...then apply $V$'"),
                   TexMobject("\\ldots\\text{then }\\Sigma"), 
                   TexMobject("\\ldots\\text{then }U")]

        for e in script: 
            e.shift(2.35*UP+RIGHT)

        if np.linalg.det(U) < 0:
            U[:,1] *= -1
            V[:,1] *= -1

        if not np.all(np.isclose(U @ np.diag(S) @ V, S)): 
            print("issue")

        self.setup()
        self.play(Write(script[0]))
        self.play(FadeOut(script[0]))
        for i,M in zip(range(1,5),[V, V.T, np.diag(S), U]):
            self.play(Write(script[i]))
            self.apply_transposed_matrix(M)
            self.play(FadeOut(script[i]))
        self.wait()

class SVM(GraphScene):

    CONFIG = {
        "background_color": WHITE,
        "x_axis_label" : '$x_{1}$', 
        "y_axis_label" : '$x_{2}$', 
        "x_min" : -2,
        "x_max" : 10,
        "y_min" : -2,
        "y_max" : 10,
        "axes_color" : BLACK, 
        "graph_origin" : ORIGIN + 3*LEFT + 1.5*DOWN,
        "function_color" : RED,
    }
        
    def randpoint(self,A=np.eye(2),b=np.array([0,0]),color="white"):
        C = Circle(color = color,
                   radius = 0.02)
        C.move_to(self.coords_to_point(*(A @ np.random.randn(2)+b)))
        return C

    def construct(self):
        self.setup_axes(animate=True)
        A1 = np.array([[1,-1/2],[1/2,1]])
        b1 = np.array([5,5])
        np.random.seed(3)
        gp = [self.randpoint(color=DARKRED) for i in range(200)]
        bp = [self.randpoint(A=A1,b=b1,color=MIDNIGHTBLUE) for i in range(200)]
        m = -1.2
        x0 = 6.6
        y0 = -2
        x1 = -1
        y1 = y0 + m*(x1 - x0)
        u = 0.87*np.array([-np.sin(np.arctan(m)), np.cos(np.arctan(m))])
        midline = Line(self.coords_to_point(x0,y0), 
                       self.coords_to_point(x1,y1),color='black')
        linelabel = TexMobject("\\boldsymbol{\\boldbeta} \\cdot \\mathbf{x} - \\alpha = 0")
        linelabel.next_to(midline, DOWN+RIGHT)
        wedge = VGroup(midline,linelabel)
        topline = Line(self.coords_to_point(x0+u[0],y0+u[1]), 
                       self.coords_to_point(x1+u[0],y1+u[1]),color='black')
        toplabel = TexMobject("\\boldsymbol{\\boldbeta} \\cdot \\mathbf{x} - \\alpha = 1")
        toplabel.next_to(topline, DOWN+RIGHT)
        topedge = VGroup(topline,toplabel)
        bottomline = Line(self.coords_to_point(x0-u[0],y0-u[1]), 
                          self.coords_to_point(x1-u[0],y1-u[1]),color='black')
        bottomlabel = TexMobject("\\boldsymbol{\\boldbeta} \\cdot \\mathbf{x} - \\alpha = -1")
        bottomlabel.next_to(bottomline, DOWN+RIGHT)
        bottomedge = VGroup(bottomline,bottomlabel)
        marginline = Line(self.coords_to_point(1.15,3.2),
                          self.coords_to_point(1.97,4.9),color=BLACK)
        marginlabel = TexMobject("2/|\\boldsymbol{\\boldbeta}|",
                                 height=0.25)
        marginlabel.move_to(self.coords_to_point(1.95,3.7))
        margin = VGroup(marginline, marginlabel)
#        axislabels = [TexMobject("x_{\\scalrel{1}{3pt}}"), TexMobject("x_{\\tiny 2}")]
#        axislabels[0].move_to(self.coords_to_point(9.5,0.5))
#        axislabels[1].move_to(self.coords_to_point(0.5,9.5))
#        for a in axislabels:
#            self.play(Write(a))
        self.play(*[GrowFromPoint(p,ORIGIN) for p in gp])
        self.play(*[GrowFromPoint(p,ORIGIN) for p in bp])
        self.play(GrowFromCenter(wedge))
        self.wait()
        self.play(Transform(wedge,topedge))
        self.wait()
        self.play(Transform(topedge,bottomedge))
        self.wait()
        self.play(GrowFromCenter(margin))
        self.wait()

class NN(Scene):

    def construct(self):
        N1 = Circle(color=BLACK, fill_color=GREEN, fill_opacity = 0.7)
        N1.move_to([-5.5,2,0])
        T1 = TexMobject("\\begin{bmatrix} -1 \\\\ 2 \\\\ 0 \\\\ 3 \\end{bmatrix}")
        T1.next_to(N1,DOWN)
        N2 = Circle(color=BLACK, fill_color=PURPLE, fill_opacity = 0.7, radius = 0.7)
        N2.next_to(N1,RIGHT)
        T2 = TexMobject("\\begin{bmatrix} -6 \\\\ 1 \\\\ -4 \\end{bmatrix}")
        T2.next_to(N2,DOWN)
        N3 = Circle(color=BLACK, fill_color=GREEN, fill_opacity = 0.7)
        N3.next_to(N2,RIGHT)
        T3 = TexMobject("\\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\end{bmatrix}")
        T3.next_to(N3,DOWN)
        N4 = Circle(color=BLACK, fill_color=PURPLE, fill_opacity = 0.7, radius = 0.7)
        N4.next_to(N3,RIGHT)
        T4 = TexMobject("\\begin{bmatrix} 6 \\\\ 11 \\\\ 4 \\\\ -3 \\\\ 0 \\end{bmatrix}")
        T4.next_to(N4,DOWN)
        N5 = Circle(color=BLACK, fill_color=GREEN, fill_opacity = 0.7)
        N5.next_to(N4,RIGHT)
        T5 = TexMobject("\\begin{bmatrix} 6 \\\\ 11 \\\\ 4 \\\\ 0 \\\\ 0 \\end{bmatrix}")
        T5.next_to(N5,DOWN)
        N6 = Circle(color=BLACK, fill_color=PURPLE, fill_opacity = 0.7, radius = 0.7)
        N6.next_to(N5,RIGHT)
        T6 = TexMobject("\\begin{bmatrix} 4 \\end{bmatrix}")
        T6.next_to(N6,DOWN)
        N7 = Circle(color=BLACK, fill_color=RED, fill_opacity = 0.7, radius = 0.5)
        N7.next_to(N6,RIGHT)
        T7 = TexMobject("\\text{cost} = (5-4)^2 = 1")
        T7.scale(0.5)
        T7.next_to(N7,DOWN)

        N = [N1, N2, N3, N4, N5, N6, N7] 
        T = [T1, T2, T3, T4, T5, T6, T7]

        for t in T:
            t.background_stroke_width = 0 

        mapnames = ["A_1", "K.", "A_2", "K.", "A_3", "C_i"]
        mapnames = [TexMobject(m) for m in mapnames]
        for m,n in zip(mapnames,N):
            m.next_to(n,UP+RIGHT, 0.5 * SMALL_BUFF)        

        ts = TexMobject("\\text{Training sample: }\\left(\\mathbf{x}_i,\\mathbf{y}_i\\right) = \\left(\\begin{bmatrix} -1 \\\\ 2 \\\\ 0 \\\\ 3  \\end{bmatrix}, [5]\\right)",background_stoke_width=0)
        ts.background_stroke_width = 0

        self.play(Write(ts))
        self.play(FadeOut(ts))
        self.play(GrowFromCenter(N[0]))
        self.play(Write(T[0]))
        self.play(Write(mapnames[0]))
        for i in range(1,7):
            self.play(GrowFromCenter(N[i]),Transform(T[0],T[i]))
            if i < 6:
                self.play(Transform(mapnames[0],mapnames[i]))

def seepoints(listOfMobjects):
    import matplotlib.pyplot as plt
    for l in listOfMobjects:
        a = l.get_all_points()
        plt.plot(a[:,0],a[:,1])
    plt.show()
