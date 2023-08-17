from manim import *

class PointToCoordsExample(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 2]).add_coordinates()
        circ = Circle(radius=0.5).shift(UR * 2)

        # get the coordinates of the circle with respect to the axes
        coords = np.around(ax.point_to_coords(circ.get_right()), decimals=2)

        label = (
            Matrix([[coords[0]], [coords[1]]]).scale(0.75).next_to(circ, RIGHT)
        )

        self.add(ax, circ, label, Dot(circ.get_right()))