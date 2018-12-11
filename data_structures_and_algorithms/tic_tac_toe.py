def is_matched(expr):
    lefty = "([{"
    righty = ')]}'
    stack = []
    for c in expr:
        if c in lefty:
            stack.append(c)
        if c in righty:
            if not stack:
                return False
            if lefty.index(stack.pop()) != righty.index(c):
                return False
    return not stack


print(is_matched("()(()){([()])}"))