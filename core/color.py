import re


def clamp(value, min_value=0, max_value=255):
    return max(min_value, min(max_value, value))


class Color:
    def __init__(self, r=0, g=0, b=0):
        self.r = clamp(r)
        self.g = clamp(g)
        self.b = clamp(b)

    @classmethod
    def from_hex(cls, hex_color: str):
        hex_color = hex_color.strip()
        if not re.match(r'^#?[0-9a-fA-F]{6}$', hex_color):
            raise ValueError("Invalid HEX color")

        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return cls(r, g, b)

    def to_array(self):
        return [self.r, self.g, self.b]

    def copy(self):
        return Color(self.r, self.g, self.b)
