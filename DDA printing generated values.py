#Wap to implement DDA Line Drawing Algorithm in Python and print genrated values
def dda_line(x1, y1, x2, y2):
    # Calculate the differences
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps needed
    steps = max(abs(dx), abs(dy))

    # Calculate the increment in x and y for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Initialize starting point
    x = x1
    y = y1

    # Generate the points
    points = []
    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment

    return points
# Example usage
x1, y1 = 2, 3
x2, y2 = 10, 7
line_points = dda_line(x1, y1, x2, y2)
print("Generated points using DDA Line Drawing Algorithm:")
for point in line_points:
    print(point)

        