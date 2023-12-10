def longest_sub_string(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    num = len(s1) - 1
    while num != 0:
        for i in range(0, len(s1) - num):
            if s1[i: i+num] in s2:
                return num
        num -= 1
    return 0
