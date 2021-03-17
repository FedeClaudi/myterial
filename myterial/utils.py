import matplotlib.cm as cm_mpl

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
