import math
from core.color import Color, clamp


class CSSFilter:
    def __init__(self):
        self.color = Color(0, 0, 0)

    def reset(self):
        self.color = Color(0, 0, 0)

    def invert(self, value):
        self.color.r = clamp((1 - value) * self.color.r + value * (255 - self.color.r))
        self.color.g = clamp((1 - value) * self.color.g + value * (255 - self.color.g))
        self.color.b = clamp((1 - value) * self.color.b + value * (255 - self.color.b))

    def sepia(self, value):
        r, g, b = self.color.r, self.color.g, self.color.b
        self.color.r = clamp(r * (1 - 0.607 * value) + g * 0.769 * value + b * 0.189 * value)
        self.color.g = clamp(r * 0.349 * value + g * (1 - 0.314 * value) + b * 0.168 * value)
        self.color.b = clamp(r * 0.272 * value + g * 0.534 * value + b * (1 - 0.869 * value))

    def saturate(self, value):
        r, g, b = self.color.r, self.color.g, self.color.b
        rw, gw, bw = 0.213, 0.715, 0.072
        self.color.r = clamp(r * (rw + value * (1 - rw)) + g * (gw - gw * value) + b * (bw - bw * value))
        self.color.g = clamp(r * (rw - rw * value) + g * (gw + value * (1 - gw)) + b * (bw - bw * value))
        self.color.b = clamp(r * (rw - rw * value) + g * (gw - gw * value) + b * (bw + value * (1 - bw)))

    def hue_rotate(self, angle):
        rad = math.radians(angle)
        cos = math.cos(rad)
        sin = math.sin(rad)

        r, g, b = self.color.r, self.color.g, self.color.b
        self.color.r = clamp(
            r * (0.213 + cos * 0.787 - sin * 0.213) +
            g * (0.715 - cos * 0.715 - sin * 0.715) +
            b * (0.072 - cos * 0.072 + sin * 0.928)
        )
        self.color.g = clamp(
            r * (0.213 - cos * 0.213 + sin * 0.143) +
            g * (0.715 + cos * 0.285 + sin * 0.140) +
            b * (0.072 - cos * 0.072 - sin * 0.283)
        )
        self.color.b = clamp(
            r * (0.213 - cos * 0.213 - sin * 0.787) +
            g * (0.715 - cos * 0.715 + sin * 0.715) +
            b * (0.072 + cos * 0.928 + sin * 0.072)
        )

    def brightness(self, value):
        self.color.r = clamp(self.color.r * value)
        self.color.g = clamp(self.color.g * value)
        self.color.b = clamp(self.color.b * value)

    def contrast(self, value):
        self.color.r = clamp((self.color.r - 128) * value + 128)
        self.color.g = clamp((self.color.g - 128) * value + 128)
        self.color.b = clamp((self.color.b - 128) * value + 128)
