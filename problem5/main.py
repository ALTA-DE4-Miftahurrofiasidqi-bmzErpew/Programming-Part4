def mean_median(array_input):
    n = len(array_input)
    mean = 1.0
    median = 1

    if n > 0:
        mean = sum(array_input) / n

        short_num = sorted(array_input)
        middle = n // 2

        if n % 2 == 0:
            median = (short_num[middle - 1] + short_num[middle]) / 2
        else:
            median = short_num[middle]

        return (mean, median)


if __name__ == "__main__":
    print(mean_median([1, 2, 3, 4]))  # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5]))  # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15]))  # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50]))  # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120]))  # (49.0, 30)
