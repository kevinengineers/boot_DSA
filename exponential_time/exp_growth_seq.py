def exponential_growth(n, factor, days):
    result = []
    result.append(n)
    for i in range(days):
        result.append(result[i] * factor)
    return result


print(exponential_growth(10, 2, 4))
