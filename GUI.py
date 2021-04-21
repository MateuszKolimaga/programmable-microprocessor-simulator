import numpy as np
import matplotlib.pyplot as plt
import random
import cv2 as cv

def draw_grid(Image, p_width, p_height, n, resq, line_thickness):
    x_ref, y_ref = 3,4

    for _ in range(p_width // 2) :
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 5
        cv.line(Image, (resq*x_start, resq*y_start), (resq*x_ref, resq*y_ref), (127, 127, 127), thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 3
        y_ref = y_start - 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 5
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 3
        y_ref = y_start + 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)

    x_start, y_start = x_ref, y_ref
    x_ref = x_start + 5
    cv.line(Image, (resq*x_start, resq*y_start), (resq*x_ref, resq*y_ref), (127, 127, 127), thickness=line_thickness)

    for _ in range(p_height - (n + 1)) :
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 3
        y_ref = y_start + 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 3
        y_ref = y_start + 4
        cv.line(Image, (resq*x_start, resq*y_start), (resq*x_ref, resq*y_ref), (127, 127, 127), thickness=line_thickness)

    for _ in range(p_width // 2) :
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 5
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 3
        y_ref = y_start + 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 5
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 3
        y_ref = y_start - 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)

    x_start, y_start = x_ref, y_ref
    x_ref = x_start - 5
    cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
            thickness=line_thickness)

    for _ in range(p_height - (n + 1)) :
        x_start, y_start = x_ref, y_ref
        x_ref = x_start - 3
        y_ref = y_start - 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)
        x_start, y_start = x_ref, y_ref
        x_ref = x_start + 3
        y_ref = y_start - 4
        cv.line(Image, (resq * x_start, resq * y_start), (resq * x_ref, resq * y_ref), (127, 127, 127),
                thickness=line_thickness)


def maze(width=59, height=40, complexity=.4, density=.9):
    n = int((width - 27)/16)
    width = 27 + n*16
    p_width = 2 + 2*n   #number of vertexes of hexagon in the straight line in the maze

    n = int((height - 24)/8)
    height = 24 + n*8
    p_height = 3 + 2*n

    resq = 10
    shape = (resq*height,resq*width)
    Image = np.zeros(shape, dtype='int32')
    line_thickness = 4

    draw_grid(Image, p_width, p_height, n, resq, line_thickness) #drawing contours of the maze

    x_ref, y_ref = 3,4 #start point from which program starts looking for the vertexes of hexagon
    Z = []

    for step in range(p_height):
        if step % 2 == 0:
            x_ref = x_ref - 3
            y_ref = y_ref + 4
            x, y= x_ref, y_ref
            for i in range(p_width):
                if i % 2 == 0:
                    x = x + 11
                    Z.append([y, x, 1])
                else:
                    x = x + 5
                    Z.append([y, x, 1])
        else:
            x_ref = x_ref + 3
            y_ref = y_ref + 4
            x, y= x_ref, y_ref
            for i in range(p_width) :
                if i % 2 == 0 :
                    x = x + 5
                    Z.append([y, x, 1])
                else :
                    x = x + 11
                    Z.append([y, x, 1])

    complexity = int(complexity*10)
    density = int(density*len(Z))

    randarr = random.sample(range(0, len(Z)), density)

    #flaga i result to zmienne pomocnicze potrzebne do okreslania kierunku, w ktory moze biec sciana
    #flag and result
    flag = 1
    result = 1

    for i in range(len(Z)):
        y,x,_ = Z[i]
        limit = 2 if random.randint(0, 10) > complexity else 3
        #limit variable describes the max number of "walls" outgoing from the current vertex
        if i in randarr:
            visible = 1
        else: visible = 0
        for j in range(complexity):
            neighbours = []
            if i % p_width == 0 and j == 0:
                result = not result
                flag = not flag

            if not flag:
                if x > 8 :neighbours.append((y, x + 5))
                if y > 8: neighbours.append((y - 4, x - 3))
                if y < shape[1] - 8 : neighbours.append((y + 4, x - 3))
                if i % 2 == result and j == complexity - 1: flag = not flag
            else:
                if x > 8: neighbours.append((y, x - 5))
                if y > 8: neighbours.append((y - 4, x + 3))
                if y < shape[1] - 8: neighbours.append((y + 4, x + 3))
                if j == complexity - 1: flag = not flag



            if len(neighbours):
                y_,x_ = neighbours[random.randint(0, len(neighbours) - 1)]
                if visible == 1 and Z[i][2] < limit:
                    cv.line(Image, (resq*x, resq*y), (resq*x_, resq*y_), (127, 127, 127), thickness=line_thickness)
                    Z[i][2] += 1

    return Image


plt.figure(figsize=(10,5))
plt.imshow(maze(200,150), cmap=plt.cm.binary, interpolation='nearest')
plt.axis('off')
plt.show()
