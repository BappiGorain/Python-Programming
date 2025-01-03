def is_palindrome(s):
    return s == s[::-1]

def is_rotational_palindrome(s):
    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_palindrome(rotated):
            return True
    return False

if __name__ == "__main__":
    test_strings = [
        "aab",
        "abc",
        "aaaa",
        "racecar",
        "carrace"
    ]

    print("Testing rotational palindrome detection:")
    for test in test_strings:
        result = is_rotational_palindrome(test)
        print(f"'{test}' is a rotational palindrome: {result}")
