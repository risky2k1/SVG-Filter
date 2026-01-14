import random
import math
from core.css_filter import CSSFilter
from core.color import Color


class Solver:
    def __init__(self, target: Color):
        self.target = target

    def loss(self, filters):
        f = CSSFilter()
        f.reset()

        f.invert(filters[0])
        f.sepia(filters[1])
        f.saturate(filters[2])
        f.hue_rotate(filters[3])
        f.brightness(filters[4])
        f.contrast(filters[5])

        return sum(abs(a - b) for a, b in zip(
            f.color.to_array(),
            self.target.to_array()
        ))

    def solve(self, iterations=1000):
        best = [0, 0, 1, 0, 1, 1]
        best_loss = self.loss(best)

        for _ in range(iterations):
            trial = [
                max(0, min(1, best[0] + random.uniform(-0.1, 0.1))),
                max(0, min(1, best[1] + random.uniform(-0.1, 0.1))),
                max(0, min(5, best[2] + random.uniform(-0.5, 0.5))),
                max(0, min(360, best[3] + random.uniform(-30, 30))),
                max(0, min(2, best[4] + random.uniform(-0.2, 0.2))),
                max(0, min(2, best[5] + random.uniform(-0.2, 0.2))),
            ]
            loss = self.loss(trial)
            if loss < best_loss:
                best, best_loss = trial, loss

        return best
