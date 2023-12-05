def generate(numRows):
    result = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)

    return result


numRows = 5
pascals_triangle = generate(numRows)
print(pascals_triangle)
