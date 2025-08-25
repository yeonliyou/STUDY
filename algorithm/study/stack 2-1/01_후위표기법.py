def change_expression(before):
    # 각 연산자의 우선순위를 딕셔너리롤 정의
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    # 연산자 스택
    stack = []
    # 최종 후위식 담을 리스트
    result = []

    for token in before:
        # 연산자인 경우
        if token in precedence.keys():
            while (
                stack  # 스택이 비어있지 않고
                and stack[-1] != '('  # top이 여는 괄호가 아니고
                # 현재 기준 토큰이 스택의 top보다 우선순위가 높다면
                and precedence.get(stack[-1], 0) >= precedence.get(token, 0)
            ):
                result.append(stack.pop())

            # while문을 만족하지 않을 경우 현재 연산자를 stack에 push하기
            stack.append(token)
        # 여는 괄호인 경우
        elif token == '(':
            # 무조건 stack에 추가
            stack.append(token)
        # 닫는 괄호인 경우
        elif token == ')':
            # 스택이 안비어있고, 여는 괄호가 아닌동안 계속 pop
            while stack and stack[-1] != '(':
                result.append(stack.pop())

            # '('을 만나면 버리기
            stack.pop()
        # 숫자나 문자인 경우
        else:
            result.append(token)

    # stack이 빌 때까지 pop 모든 연산자를 pop해서 result에 추가
    while stack:
        result.append(stack.pop())

    return "".join(result)


print(change_expression("(A*B)/B+C"))