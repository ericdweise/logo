from math import cos, pi, sin
from circle import Circle

OUTPUT_FILE = 'TEST.svg'

BASE_RADIUS = 32
CANOPY_ITER = 4
FILL='#125E87'

xmin = float('Inf')
xmax = -float('Inf')
ymin = float('Inf')
ymax = -float('Inf')


##############
### CANOPY ###
##############
def canopy_to_str(cx, cy, rad):
    return(f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="{FILL}" />\n')

canopy_str = ''

# Initialize lists for building circles
parents = []
children = []

children.append(Circle(0, 0, BASE_RADIUS, None))
canopy_str += canopy_to_str(0,0,BASE_RADIUS)

for step in range(1, CANOPY_ITER):
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

            RAD = int(round(parent.radius/2))

            CX = int(round(parent.x_center + (parent.radius + RAD)*cos(radians)))
            CY = int(round(parent.y_center + (parent.radius + RAD)*sin(radians)))

            children.append(Circle(CX, CY, RAD, grow_dir))

            canopy_str += canopy_to_str(CX, CY, RAD)

            xmin = min(xmin, CX - RAD)
            xmax = max(xmax, CX + RAD)
            ymin = min(ymin, CY - RAD)
            ymax = max(ymax, CY + RAD)

        
#############
### Trunk ###
#############
trunk_str = ''

height = 4*BASE_RADIUS
offset = 3*BASE_RADIUS/4
offset2 = BASE_RADIUS/4
offset3 = 2*offset2
width_1 = BASE_RADIUS/4
width_2 = BASE_RADIUS/16
width_3 = BASE_RADIUS/32

trunk_str += f'<rect x="{-offset}" y="0" height="{height}" width="{width_2}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{offset-width_2}" y="0" height="{height}" width="{width_2}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{-width_1/2}" y="0" height="{height}" width="{width_1}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{ offset2}"   y="{3*BASE_RADIUS/2}" height="{5*BASE_RADIUS/2}" width="{width_3}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{-offset2}"   y="{3*BASE_RADIUS/2}" height="{5*BASE_RADIUS/2}" width="{width_3}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{ offset3}"   y="{2*BASE_RADIUS}" height="{2*BASE_RADIUS}" width="{width_3}" fill="{FILL}" />\n'
trunk_str += f'<rect x="{-offset3}"   y="{2*BASE_RADIUS}" height="{2*BASE_RADIUS}" width="{width_3}" fill="{FILL}" />\n'

ymax = max(ymax, height)



with open(OUTPUT_FILE, 'w') as f:
    f.write('<?xml version="1.0" encoding="utf-8" ?>\n')
    f.write(f'<svg baseProfile="full" viewBox="{xmin} {ymin} {xmax-xmin} {ymax-ymin}" height="100%" version="1.1" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
    f.write('<defs />\n')

    # Canopy
    f.write(canopy_str)

    # Tree Trunk
    f.write(trunk_str)

    f.write('</svg>\n')
