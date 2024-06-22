def draw_xyz(N):
    pattern = ""
    for i in range(N):
        for j in range(1, N + 1):
            x = i * N
            num = x + j
            if num % 3 == 0:
                pattern += "X "
            elif num % 2 == 1:
                pattern += "Y "
            else:
                # print("Z", end="  ")
                pattern += "Z "

        pattern += "\n"

    return pattern


# print(draw_xyz(3))
# print(draw_xyz(5))
if __name__ == "__main__":
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """

    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
