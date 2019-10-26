"""
"""

class Circle(object):
    """
    """

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
