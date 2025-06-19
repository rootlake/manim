from manimlib import *
import numpy as np

class SimpleDemo(Scene):
    def construct(self):
        # Use classic 3B1B font
        text_top = Text("Welcome to", font="CMU Serif")
        text_bottom = Text("Manim!", font="CMU Serif")
        text_group = VGroup(text_top, text_bottom).arrange(DOWN)
        
        # Create circle that fits around the text
        circle = Circle()
        circle.surround(text_group)
        circle.scale(1.2)
        circle.set_color(BLUE)
        circle.set_fill(BLUE, opacity=0.3)
        
        # Create hexagon that surrounds the circle
        hexagon = RegularPolygon(n=6)
        hexagon.surround(circle)
        hexagon.scale(1.1)
        hexagon.set_color(YELLOW)
        hexagon.set_fill(YELLOW, opacity=0.2)
        
        # Create area equations with classic font
        r = circle.get_width() / 2  # radius of circle
        circle_area = Text("Circle Area = πr²", font="CMU Serif")
        circle_area.scale(0.8)
        circle_area.set_color(BLUE)
        circle_area.to_edge(LEFT).shift(UP)
        
        hex_area = Text("Hexagon Area = 2√3 r²", font="CMU Serif")
        hex_area.scale(0.8)
        hex_area.set_color(YELLOW)
        hex_area.next_to(circle_area, DOWN, aligned_edge=LEFT)
        
        diff_area = Text("Difference ≈ 0.1 r²", font="CMU Serif")
        diff_area.scale(0.8)
        diff_area.set_color(GREEN)
        diff_area.next_to(hex_area, DOWN, aligned_edge=LEFT)
        
        # Initial animations
        self.play(
            Write(text_top),
            Write(text_bottom),
            run_time=2
        )
        
        self.play(
            ShowCreation(circle),
            Write(circle_area),
            run_time=1.5
        )
        
        self.play(
            ShowCreation(hexagon),
            Write(hex_area),
            run_time=1.5
        )
        
        # Create 6 difference regions
        difference_pieces = VGroup()
        angles = np.linspace(0, TAU, 7)[:-1]  # 6 evenly spaced angles
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE_B, PURPLE]
        
        # Create an AnnularSector for each piece
        for angle, color in zip(angles, colors):
            piece = AnnularSector(
                inner_radius=circle.get_width()/2,
                outer_radius=hexagon.get_width()/2,
                angle=TAU/6,
                start_angle=angle,
                fill_opacity=0.5,
                stroke_width=0
            )
            piece.set_color(color)
            difference_pieces.add(piece)
        
        # Highlight each piece sequentially
        for i, piece in enumerate(difference_pieces):
            self.play(
                FadeIn(piece),
                run_time=0.5
            )
            if i == len(difference_pieces) - 1:
                self.play(Write(diff_area), run_time=1)
        
        # Pause to appreciate the scene
        self.wait()
        
        # Shrink and spin everything to a point
        everything = VGroup(text_group, circle, hexagon, difference_pieces)
        equations = VGroup(circle_area, hex_area, diff_area)
        
        self.play(
            everything.animate.scale(0).move_to(ORIGIN).rotate(TAU*2),
            FadeOut(equations),
            rate_func=smooth,
            run_time=2
        )
        self.wait(0.5)
