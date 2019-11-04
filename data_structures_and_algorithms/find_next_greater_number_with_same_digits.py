def find_next(digits, n):

    f = False
    length = n
    while n > 0:
        n -= 1
        for i in range(n - 1, 0, -1):
            if digits[i] < digits[n]:
                f = True
                digits[i], digits[n] = digits[n], digits[i]
                temp = sorted(digits[(i + 1): n + 1])
                for j in range(i, n):
                    digits[j + 1] = temp[j - i]
                break
        if f:
            break
    if not f:
        print("Could not find the next greater number with same set of digits")
        return 0

    return digits[0:length]


if __name__ == "__main__":
    number = "534976"
    digits = [int(x) for x in str(number)]
    result = find_next(digits, len(digits))
    print(result)
