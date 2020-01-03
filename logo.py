from math import cos, pi, sin

from circle import Circle


class Logo(object):
    """
    Class that builds the logo graphic.
    """

    contents = []


    # TODO: Add rotation by theta, compounding every iteration.
    def canopy(self, n_iter, radius=128, angle=0):
        """
        Will create the 'canopy' of the tree. This is the fractal built
        out of circles and represents the leaves of the logo.

        Args:
            n_iter: The number of iterations of the fractal rendered
                before termination. Must be an integer > 0.
            radius: The radius of the first (largest) circle in the
                fractal. [OPTIONAL, default=128)
            angle: Each iteration of the fractal is rotated from its
                parent by this many degrees.
        """

        # Find center of first circle
        cx = 3*radius
        cy = 3*radius

        # Initialize lists for building circles
        parents = []
        children = []

        children.append(Circle(cx, cy, radius, 270))
        angle_sum = 0

        for step in range(1, n_iter):

            radius = radius/2
            angle_sum += angle

            self.contents.extend(parents)
            parents = children
            children = []

            for parent in parents:

                for grow_dir in (0, 90, 180, 270):
                    radians = grow_dir*pi/180
                    if abs(parent.grow_dir - grow_dir) == 180:
                        continue

                    x_center = parent.x_center + 3*radius*cos(angle_sum + radians)
                    y_center = parent.y_center + 3*radius*sin(angle_sum + radians)

                    children.append(Circle(x_center, y_center, radius, grow_dir))

        self.contents.extend(parents)
        self.contents.extend(children)


    # TODO: Add method to build tree trunk


    # TODO: Add method to build roots


    def write_svg(self, path, **kwargs):
        """
        Will convert self.contents into XML and write this to a file.

        Args:
            path: File location where the SVG file will be saved.

        Kwargs:
            Any key word arguments supported by svgwrite.Drawing.save().
            For example: fill='blue'.
        """
        import svgwrite

        drawing = svgwrite.Drawing(filename=path)

        for elt in self.contents:
            if type(elt==Circle):
                drawing.add(svgwrite.shapes.Circle(
                        center=(elt.x_center,elt.y_center),
                        r=elt.radius,
                        **kwargs))
            else:
                raise Exception('Unknown class in contents: {}'.format(type(elt)))

        drawing.save()


if __name__ == '__main__':
    l = Logo()
    l.canopy(8, 128, 10*pi/180)
    l.write_svg('test-2-with-filter.svg', fill='blue')
