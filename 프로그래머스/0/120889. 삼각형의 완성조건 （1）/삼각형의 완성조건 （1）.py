def solution(sides):
    answer = 0
    s_sides = sorted(sides, reverse =True)
    if s_sides[0]< s_sides[1]+s_sides[2]:
        return 1
    elif s_sides[0] >= s_sides[1]+s_sides[2]:
        return 2