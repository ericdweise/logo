class circle(object):

    x_center = None # Absolute x-coordinate for the center of this circle
    y_center = None # Absolute y-coordinate for the center of this circle
    radius = None

    # grow_dir indicates the direction that the circle is growing in. This
    # can take any value in {0,1,2,3} with the following meanings:
    # 0 - circle is growing in the +x direction
    # 1 - circle is growing in the -y direction
    # 2 - circle is growing in the -x direction
    # 3 - circle is growing in the +y direction
    grow_dir = None

    # indicates the iteration in which this circle was generated
    order = None

    def __init__(self, x_center, y_center, radius, grow_dir):
        """
        """
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        self.grow_dir = grow_dir

    def introspect(self):
        print('introspecting circle:')
        print('  x-center: {}'.format(self.x_center))
        print('  y-center: {}'.format(self.y_center))
        print('  radius:   {}'.format(self.radius))
        print('  grow-dir: {}'.format(self.grow_dir))


def canopy(n_iter):

    parents = []
    children = []
    svg_contents = []

    children.append(circle(0, 0, 2**n_iter, 3))

    for step in range(1, n_iter):

        radius = 2**(n_iter - step)

        svg_contents.extend(parents)
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
                children.append(circle(x_center, y_center, radius, grow_dir))

    svg_contents.extend(children)

    return svg_contents


def translate(svg_list, dx=0, dy=0):
    """
    Will move all contents in an SVG list by given deltas in x and y.
    """
    pass


def scale(svg_list, m):
    """
    Will scale all contents in an SVG list by a given factor, m. Stationary point is at (0,0)
    """
    pass


def write_svg_file(svg_contents, path):
    """
    Will convert contents of the list svg_contents into XML and write this to a file.
    """
    pass
