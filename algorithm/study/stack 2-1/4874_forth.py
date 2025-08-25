import sys
sys.stdin = open("sample_input.txt")

T = int(input())

precedence_list = ['+', '-', '*', '//', '/', '%', '**']

for t in range(1, T + 1):
    # 숫자를 넣을 stack
    stack = []

    # 입력 받기
    input_list = list(input().split())

    # flag 초기화
    result = 0

    ###################################
    ## 근데 이 경우 빼보니까 없어도 통과됨
    ## 아 근데 걍 애초에 그냥 없어도 되네
    ## 문제를 잘읽자 ^^
    ###################################
    # 애초에 연산자가 없는 경우
    '''
    cnt_pre = 0
    for check in precedence_list:
        if check in input_list:
            cnt_pre += 1
    # 연산자가 한번도 없었다면
    if cnt_pre == 0:
        result = 'error'
    '''

    for curr in input_list:
        # 현재 검사하는 요소가 연산자인 경우
        if curr in precedence_list:
            # 스택에 최소 2개의 숫자가 있을 때
            if len(stack) >= 2:

                # 계산할 2개의 숫자 저장
                right = int(stack.pop())
                left = int(stack.pop())

                # 연산자가 뭐냐에 따라
                if curr == '+':
                    stack.append(left + right)
                elif curr == '-':
                    stack.append(left - right)
                elif curr == '*':
                    stack.append(left * right)
                elif curr == '**':
                    stack.append(left ** right)

                # 0으로 나누는 것은 불가능한 연산이기에 따로 예외처리
                elif curr == '//':
                    if right == 0:
                        result = 'error'
                        break
                    else:
                        stack.append(left // right)
                elif curr == '/':
                    if right == 0:
                        result = 'error'
                        break
                    else:
                        stack.append(left / right)
                elif curr == '%':
                    if right == 0:
                        result = 'error'
                        break
                    else:
                        stack.append(left % right)

            # 스택에 연산할 숫자가 2개가 안될때 + 애초에 인풋에 연산자만 있던 경우
            else:
               result = 'error'
               break

        # 종료조건인 경우
        elif curr == '.':
            # 예외들 : 처음부터 인풋에 .만 있는 경우 or stack에 남아있는 숫자가 여러개인 경우
            if len(stack) != 1:
                result = 'error'
            break
        # 숫자인 경우
        else:
            try:
                # 현재 요소 정수로 바꿔서 stack에 추가
                stack.append(int(curr))
            # 정수로 변환이 안되는 이 외의 문자의 경우
            except:
                result = 'error'
                break

    # 만약 error가 존재하면 그대로 출력
    if result != 0:
        print(f"#{t}", result)
    # 존재하지 않으면 stack의 마지막 값출력
    ##############################################################
    ############ 문제 조건을 잘 읽자 ^^ 정수로 출력하라잖니? ############
    ##############################################################
    else:
        print(f"#{t}", int(stack.pop()))
