def play_with_asterisk(n):
    pattern = ""
    for i in range(n):
        for j in range(n - i - 1):
            pattern += " "

        for j in range(i + 1):
            pattern += "* "
        pattern += "\n"

    return pattern


# print(play_with_asterisk(5))

if __name__ == "__main__":
    print(play_with_asterisk(5))
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
