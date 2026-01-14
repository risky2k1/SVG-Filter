from core.color import Color
from core.solver import Solver

target = Color.from_hex("#ff5722")
solver = Solver(target)
result = solver.solve()

print(f"""
filter: invert({result[0] * 100:.0f}%)
        sepia({result[1] * 100:.0f}%)
        saturate({result[2] * 100:.0f}%)
        hue-rotate({result[3]:.0f}deg)
        brightness({result[4] * 100:.0f}%)
        contrast({result[5] * 100:.0f}%);
""")
