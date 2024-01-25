matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed_matrix = zip(*matrix)
res = [list(row) for row in transposed_matrix]

print(res)
