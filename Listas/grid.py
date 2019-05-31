# Rota el grid a la derecha

image = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

rotate = []

for i in range(len(image[0])):
    rotate.append([space[i] for space in image])

for j in range(len(image)):
    print(image[j])

for k in range(len(rotate)):
    print(rotate[k])