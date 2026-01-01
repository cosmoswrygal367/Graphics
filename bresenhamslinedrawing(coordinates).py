"""
bresenhamslinedrawing.py

Simple Bresenham line algorithm and small demo.
"""

def bresenham(x0, y0, x1, y1):
    """
    Bresenham's line algorithm between integer points (x0,y0) and (x1,y1).
    Returns a list of (x, y) points on the line (inclusive).
    """
    points = []
    x, y = x0, y0
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy  # error term

    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:  # move in x
            err += dy
            x += sx
        if e2 <= dx:  # move in y
            err += dx
            y += sy
    return points

if __name__ == "__main__":
    # quick demonstration
    # change these to try different endpoints
    x0, y0 = 2, 2
    x1, y1 = 18, 10

    pts = bresenham(x0, y0, x1, y1)
    print("Points on the line:")
    for p in pts:
        print(p)

    # optional visualization if matplotlib is available
    try:
        import matplotlib.pyplot as plt
        xs, ys = zip(*pts)
        plt.figure(figsize=(6,4))
        plt.scatter(xs, ys, c='black')
        plt.plot([x0, x1], [y0, y1], c='lightgray', linestyle='--')  # reference
        plt.gca().invert_yaxis()  # match typical screen coordinates if desired
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title(f"Bresenham line from ({x0},{y0}) to ({x1},{y1})")
        plt.grid(True)
        plt.show()
    except Exception:
        pass