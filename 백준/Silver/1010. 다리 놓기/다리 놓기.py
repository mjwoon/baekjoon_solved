def factorial(t):
    case = 1
    for i in range(1, t + 1):
        case *= i
    return case

testcase = int(input())

for _ in range(testcase):
    west, east = map(int, input().split())
    bridge = factorial(east) // (factorial(west) * factorial(east - west))

    print(bridge)
