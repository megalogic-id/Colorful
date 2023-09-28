import colorsys


def matching_gradient(hex_color):
    # Create a gradient by manipulating hue slightly
    return [adjust_hue(hex_color, i*0.05) for i in range(0, 10, 2)]


def spot_palette(hex_color):
    # Random spots across the spectrum
    return [adjust_hue(hex_color, i*0.1) for i in range(0, 10, 2)]


def twisted_spot_palette(hex_color):
    # A different twist on spot adjustments
    return [adjust_brightness(adjust_hue(hex_color, i*0.1), i*0.05) for i in range(0, 5, 2)]


def classy_palette(hex_color):
    # Just some arbitrary adjustments for variety
    return [adjust_brightness(adjust_hue(hex_color, i*0.1), -i*0.05) for i in range(5)]


def small_switch_palette(hex_color):
    # A tighter switch between adjustments
    return [adjust_brightness(hex_color, i*0.05*(-1)**i) for i in range(5)]


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def adjust_brightness(hex_color, factor):
    rgb = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(*[x/255.0 for x in rgb])
    l = max(min(l + factor, 1), 0)
    rgb_adjusted = [int(x*255) for x in colorsys.hls_to_rgb(h, l, s)]
    return rgb_to_hex(rgb_adjusted)


def adjust_hue(hex_color, factor):
    rgb = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(*[x/255.0 for x in rgb])
    h = (h + factor) % 1
    rgb_adjusted = [int(x*255) for x in colorsys.hls_to_rgb(h, l, s)]
    return rgb_to_hex(rgb_adjusted)


def complementary_colors(hex_color):
    """Generate a palette of complementary colors."""
    h, l, s = hex_to_hls(hex_color)
    complementary_hue = (h + 0.5) % 1.0
    return [hex_color, hls_to_hex(complementary_hue, l, s)]


def triadic_colors(hex_color):
    """Generate a triadic color palette."""
    h, l, s = hex_to_hls(hex_color)
    return [
        hex_color,
        hls_to_hex((h + 1/3) % 1.0, l, s),
        hls_to_hex((h + 2/3) % 1.0, l, s)
    ]


def analogous_colors(hex_color):
    """Generate an analogous color palette."""
    h, l, s = hex_to_hls(hex_color)
    return [
        hls_to_hex((h - 0.05) % 1.0, l, s),
        hex_color,
        hls_to_hex((h + 0.05) % 1.0, l, s)
    ]


def hex_to_hls(hex_color):
    """Convert HEX to HLS color space."""
    rgb = hex_to_rgb(hex_color)
    return colorsys.rgb_to_hls(*[x/255.0 for x in rgb])


def hls_to_hex(h, l, s):
    """Convert HLS to HEX color."""
    rgb = colorsys.hls_to_rgb(h, l, s)
    return rgb_to_hex([int(x*255) for x in rgb])