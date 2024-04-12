colours = [["r","g","g","g","g","g","r"],
            ["y","r","r","r","r","r","y"],
            ["y","y","r","r","r","y","y"],
           ["b","b","b","r","b","b","b"],
            ["y","y","r","r","r","y","y"],
            ["y","r","r","r","r","r","y"],
           ["r","g","g","g","g","g","r"]]
c = "bl"
row, col = len(colours), len(colours[0])
target = "r"
def bfs(r,c):
    if r > row or r < 0 or c > col or c < 0:
        return
    if colours[r][c] == target:
        colours[r][c] = "bl"
        up = bfs(r-1, c)
        down = bfs(r+1, c)
        left = bfs(r, c-1)
        right = bfs(r, c+1)
    return
bfs(3, 3)
for r in range(row):
    for c in range(col):
        print(colours[r][c], end="    ")
    print()