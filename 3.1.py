import matplotlib.pyplot as plt
import numpy as np

# def get_first(r, c):
#     result = []
#     seen = [[False] * c for _ in range(r)]
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     x = y = di = 0

#     for _ in range(r * c):
#         result.append((x, y))
#         seen[x][y] = True
#         next_row, next_col = x + dr[di], y + dc[di]
#         if 0 <= next_row < r and 0 <= next_col < c and not seen[next_row][next_col]:
#             x, y = next_row, next_col
#         else:
#             di = (di + 1) % 4
#             x, y = x + dr[di], y + dc[di]

#     return [x * c + y for x, y in result]

def get_second(r, c):
    grid = np.arange(r * c).reshape(r, c)
    result = []
    for i in range(r):
        if i % 2 == 0:
            result.extend(grid[i, :])
        else:
            result.extend(grid[i, ::-1])
    return result

c = int(input('Введите кол-во квадратов по строке: '))
r = int(input('Введите кол-во квадратов по столбцов: '))
method = int(input('Выберите способ окрашивания: по спирали - 1, змейкой - 2: '))
w = 200
h = 100
rects = []
rw, rh = w / c, h / r
for i in range(r):
    for j in range(c):
        rects.append(((j * rw, i * rh), rw, rh))
num_rects = len(rects)
colors = plt.cm.rainbow(np.linspace(0, 1, num_rects))

# if method==1:
#     result = get_first(r, c) 
# else:
result = get_second(r, c) 

fig, ax = plt.subplots()
ax.set_xlim(0, w)
ax.set_ylim(0, h)
patch = []
for i, ((x, y), rw, rh) in enumerate(rects):
    rect = plt.Rectangle((x, y), rw, rh, edgecolor='black', facecolor=colors[result.index(i)])
    patch.append(rect)
    ax.add_patch(rect)
plt.show()
