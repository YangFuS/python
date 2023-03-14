import time

ops_priority = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "(": -1,
    ")": -1,
}


def str_to_int(s: str) -> int:
    flag = 1
    res = 0
    if len(s) == 0:
        raise Exception("error str")
    if s[0] == '-':
        flag = -1
        s = s[1:]
    if s[:2].upper() == "0x".upper():
        res = int(s, base=16)
    else:
        res = int(s)
    return res * flag


def check_is_op(s: str) -> bool:
    if s in ops_priority.keys():
        return True
    return False


def infix_to_suffix(s: str) -> str:
    """
    中缀表达式转后缀表达式
    :param s: 需要运算的中缀表达式
    :return: 对应的后缀表达式
    """
    stack = []
    res = ""
    ops = s.split(' ')
    if len(ops) == 0:
        return ""
    for op in ops:
        if check_is_op(op):
            if op == "(":
                stack.append(op)
            elif op == ")":
                # 括号内运算符全部出栈
                while stack[-1] != "(":
                    temp = stack.pop(-1)
                    res = res + temp + " "
                stack.pop(-1)
            else:
                while stack and ops_priority[stack[-1]] >= ops_priority[op]:
                    temp = stack.pop(-1)
                    res = res + temp + " "
                stack.append(op)
        else:
            res = res + op + " "
    while stack:
        temp = stack.pop(-1)
        res = res + temp + " "
    res = res.strip()
    return res


def op_2_nums(op: str, left, right) -> float:
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right
    else:
        raise Exception(f"not support op:{op}")


def calc_suffix(s: str) -> float:
    """
    计算后缀表达式结果
    :param s: 后缀表达式
    :return: 运算结果
    """
    stack = []
    res = 0
    ops = s.split(' ')
    if len(ops) == 0:
        raise Exception("error representation")
    for op in ops:
        if check_is_op(op):
            if len(stack) < 2:
                raise Exception("error representation")
            right_num = stack.pop(-1)
            left_num = stack.pop(-1)
            res = op_2_nums(op, left_num, right_num)
            stack.append(res)
        else:
            stack.append(str_to_int(op))
    return res


s1 = "9 + ( 0xe3 - 1 ) * 3 + 10 / 2"
print(time.time())
s_suffix = infix_to_suffix(s1)
print(s_suffix)
res = calc_suffix(s_suffix)
print(time.time())
print(res)
print(time.time())
print(9 + (0xe3 - 1) * 3 + 10 / 2)
print(time.time())
