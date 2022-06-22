def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False
    stack = []

    for  bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "]})":
            peeked = stack[-1]
            if (bracket ==")" and peeked == "(") or\
                    (bracket =="}" and peeked == "{") or\
                    (bracket == "]" and peeked == "["):
                stack.pop()
            else:
                return False
        else:
            return False
    return True

paired = bracket_pair("{}({[]})")
print(paired)