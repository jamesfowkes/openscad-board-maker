""" openscad-board-maker.py

Usage:
    openscad-board-maker.py <l> <w>

"""

from solid import *

import docopt

if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    l = float(args["<l>"])
    w = float(args["<w>"])

    r = 4

    rect1 = cube(size=(l, w - 2*r, 1.6), center=True)
    rect2 = cube(size=(l - 2*r, w, 1.6), center=True)

    corner_centers = (l/2-r, w/2-r)

    corners = [
        translate(v=(corner_centers[0], corner_centers[1], 0)) (
            cylinder(r=r, h=1.6, center=True) - hole()(cylinder(r=1.5, h=1.7, center=True))
        ),
        translate(v=(-corner_centers[0], corner_centers[1], 0)) (
            cylinder(r=r, h=1.6, center=True) - hole()(cylinder(r=1.5, h=1.7, center=True))
        ),
        translate(v=(corner_centers[0], -corner_centers[1], 0)) (
            cylinder(r=r, h=1.6, center=True) - hole()(cylinder(r=1.5, h=1.7, center=True))
        ),
        translate(v=(-corner_centers[0], -corner_centers[1], 0)) (
            cylinder(r=r, h=1.6, center=True) - hole()(cylinder(r=1.5, h=1.7, center=True))
        )
    ]

    a = union()(rect1, rect2, *corners)

    scad_render_to_file(a, file_header='$fn = 48;', include_orig_code=True)