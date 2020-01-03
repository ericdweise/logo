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

        # Convert angle to radians
        angle = angle*pi/180

        # Find center of first circle
        cx = 3*radius
        cy = 3*radius

        # Initialize lists for building circles
        parents = []
        children = []

        children.append(Circle(cx, cy, radius, None))
        angle_sum = 0

        for step in range(1, n_iter):

            angle_sum += angle

            self.contents.extend(parents)
            parents = children
            children = []

            for parent in parents:
                for grow_dir in (0, 90, 180, 270):
                    radians = grow_dir*pi/180
                    
                    if parent.grow_dir is None:
                        if grow_dir == 90:
                            continue
                    elif abs(parent.grow_dir - grow_dir) == 180:
                        continue

                    rad = parent.radius/2
                    if not parent.grow_dir == None:
                        if angle > 0:
                            if grow_dir - parent.grow_dir in (90, -270):
                                rad = (1-0.02*angle*180/pi)*rad
                        elif angle < 0:
                            if parent.grow_dir - grow_dir in (90, -270):
                                rad = (1+0.02*angle*180/pi)*rad

                    xc = parent.x_center + (parent.radius + rad)*cos(angle_sum + radians)
                    yc = parent.y_center + (parent.radius + rad)*sin(angle_sum + radians)

                    children.append(Circle(xc, yc, rad, grow_dir))

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
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--iterations', type=int, default=8,
            help='The number of iterations to be rendered in the fractal.')
    parser.add_argument('-b', '--base-radius', type=int, default=128,
            help='The radius of the largest circle, in px.')
    parser.add_argument('-r', '--rotate', type=int, default=0,
            help='Rotate the canopy by this many degrees at each level.')
    parser.add_argument('-f', '--file',
            help='Save output to a file.')

    args = parser.parse_args()

    l = Logo()
    l.canopy(args.iterations, args.base_radius, args.rotate)
    if args.file:
        l.write_svg(args.file, fill='blue')
