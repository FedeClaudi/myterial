import matplotlib.cm as cm_mpl
import numpy as np


def rgb2hex(rgb):
    """Convert RGB to Hex color."""
    h = '#%02x%02x%02x' % (int(rgb[0]*255),int(rgb[1]*255),int(rgb[2]*255))
    return h

def hex2rgb(hx):
        h = hx.lstrip("#")
        rgb255 = [int(h[i : i + 2], 16) for i in (0, 2, 4)]
        return (rgb255[0]/255., rgb255[1]/255., rgb255[2]/255.)

def make_palette(c1, c2, N):
    c1 = np.array(hex2rgb(c1))
    c2 = np.array(hex2rgb(c2))
    cols = []
    for f in np.linspace(0, 1, N, endpoint=True):
        c = c1 * (1 - f) + c2 * f
        cols.append(rgb2hex(c))
    return cols


def map_color(value, name="jet", vmin=None, vmax=None):
    """Map a real value in range [vmin, vmax] to a (r,g,b) color scale.
    :param value: scalar value to transform into a color
    :type value: float, list
    :param name: color map name (Default value = "jet")
    :type name: str, matplotlib.colors.LinearSegmentedColorMap
    :param vmin:  (Default value = None)
    :param vmax:  (Default value = None)
    :returns: return: (r,g,b) color, or a list of (r,g,b) colors.
    """
    if vmax < vmin:
        raise ValueError("vmax should be larger than vmin")

    mp = cm_mpl.get_cmap(name=name)

    value -= vmin
    value /= vmax - vmin
    if value > 0.999:
        value = 0.999
    elif value < 0:
        value = 0
    return mp(value)[0:3]
