from circle import circle


def canopy(n_iter):

    parents = []
    children = []
    contents = []

    children.append(circle(0, 0, 2**n_iter, 3))

    for step in range(1, n_iter):

        radius = 2**(n_iter - step)

        contents.extend(parents)
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

    contents.extend(parents)
    contents.extend(children)

    return contents


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


def write_svg_file(contents, path, **kwargs):
    """
    Will convert contents of the list contents into XML and write this to a file.
    """
    import svgwrite

    drawing = svgwrite.Drawing(filename=path)

    for elt in contents:
        if type(elt==circle):
            drawing.add(svgwrite.shapes.Circle(
                    center=(elt.x_center,elt.y_center),
                    r=elt.radius,
                    **kwargs))
        else:
            raise Exception('Unknown class in contents: {}'.format(type(elt)))

    # Set SVG viewbox to include entire image
    boundary = find_boundary(contents)
    drawing.viewbox(
            minx=boundary['xmin'],
            miny=boundary['ymin'],
            width=boundary['xmax'] - boundary['xmin'],
            height=boundary['ymax'] - boundary['ymin'])

    drawing.save()


def find_boundary(contents):
    xmax = -float('inf')
    ymax = -float('inf')
    xmin = float('inf')
    ymin = float('inf')

    for elt in contents:
        if type(elt) == circle:
            if xmax < elt.x_center + elt.radius:
                xmax = elt.x_center + elt.radius
            if xmin > elt.x_center - elt.radius:
                xmin = elt.x_center - elt.radius
            if ymax < elt.y_center + elt.radius:
                ymax = elt.y_center + elt.radius
            if ymin > elt.y_center - elt.radius:
                ymin = elt.y_center - elt.radius
        else:
            raise Exception('Unknown class in contents: {}'.format(type(elt)))

        return {'xmax': xmax, 'xmin': xmin, 'ymax': ymax, 'ymin': ymin}


if __name__ == '__main__':
    c = canopy(3)
    write_svg_file(c, 'test.svg', fill='blue')
