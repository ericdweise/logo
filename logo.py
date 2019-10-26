from circle import Circle


class Logo(object):
    """
    Class that builds the logo graphic
    """

    contents = []


    def canopy(self, n_iter, radius=None):

        # Find initial radius if not provided:
        if radius == None:
            radius = 2**(n_iter)

        # Find center of first circle
        cx = 3*radius
        cy = 3*radius

        # Initialize lists for building circles
        parents = []
        children = []

        children.append(Circle(cx, cy, radius, 3))

        for step in range(1, n_iter):

            radius = radius/2

            self.contents.extend(parents)
            parents = children
            children = []

            for parent in parents:
                for grow_dir in range(4):
                    if abs(parent.grow_dir - grow_dir) == 2:
                        continue
                    if grow_dir == 0:
                        x_center = parent.x_center + radius + parent.radius
                        y_center = parent.y_center
                    elif grow_dir == 1:
                        x_center = parent.x_center
                        y_center = parent.y_center + radius + parent.radius
                    elif grow_dir == 2:
                        x_center = parent.x_center - radius - parent.radius
                        y_center = parent.y_center
                    elif grow_dir == 3:
                        x_center = parent.x_center
                        y_center = parent.y_center - radius - parent.radius
                    children.append(Circle(x_center, y_center, radius, grow_dir))

        self.contents.extend(parents)
        self.contents.extend(children)


    def write_svg(self, path, **kwargs):
        """
        Will convert self.contents into XML and write this to a file.
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
    l.canopy(8, 128)
    l.write_svg('test.svg', fill='blue')
