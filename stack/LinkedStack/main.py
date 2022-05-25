from Stack import Stack


def reverse(s):
    stack = Stack()
    for i in range(len(s)):
        stack.push(s[i])
    res = ""
    for _ in range(stack.size()):
        res += stack.pop()

    return res


input = input("Input: ")
print(reverse(input))
