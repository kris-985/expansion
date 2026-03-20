def linear_prediction(years, values, target_year):
    n = len(years)

    sum_x = sum(years)
    sum_y = sum(values)
    sum_xy = sum(x * y for x, y in zip(years, values))
    sum_xx = sum(x * x for x in years)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return int(slope * target_year + intercept)