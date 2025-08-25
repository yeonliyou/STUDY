# 후위 표기식으로 바꾸는 함수
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


def calculate_expression(expression):

    # 피연산자 저장할 스택
    stack = []

    # 인풋 표현식 반복문
    for token in expression:
        # 토큰이 숫자일때
        if token.isdigit():
            # 스택에 정수로 바꿔서 넣기
            stack.append(int(token))

        # 토큰이 연산자일때
        else:
            # 스택에서 피연산자 2개를 pop
            right = stack.pop()
            left = stack.pop()

            # 토큰에 종류에 따라 연산 수행
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                # 나누기의 경우 0으로 나누는 상황을 고려할 수도 있음 (여기서는 생략)
                result = left / right
            elif token == '^':
                result = left ** right
            else:
                # 이상한 연산자가 들어올 경우
                raise ValueError('error')

            # 연산 결과 result를 다시 스택에 push
            stack.append(result)

    # 연산 종료 후에 마지막 값이 답
    return stack.pop()


import sys
sys.stdin = open("input.txt")

for t in range(1,11):
    input_len = int(input())
    before = list(input())

    after_expression = change_expression(before)
    result = calculate_expression(after_expression)

    print(f"#{t}", result)