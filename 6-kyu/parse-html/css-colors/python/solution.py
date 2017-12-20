def parse_html_color(color):
    channels = 'rgb'
    if color.startswith('#') and len(color) == 7:
        hex_digits = (color[i: i+2] for i in range(1, 7, 2))
        return {c: int(h, 16) for c, h in zip(channels, hex_digits)}
    elif color.startswith('#') and len(color) == 4:
        hex_digits = (color[i] for i in range(1, 4))
        return {c: int(h*2, 16) for c, h in zip(channels, hex_digits)}
    else:
        return parse_html_color(PRESET_COLORS[color.lower()])