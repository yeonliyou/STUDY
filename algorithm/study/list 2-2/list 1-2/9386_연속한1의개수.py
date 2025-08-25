T = int(input())

for t in range(1, T+1):
     N = int(input())
     number_list = list(input())

     #연속한 1의 개수 중 최대값 초기화
     max_length = 0

     #1을 넣을 임시 리스트
     one_list = []
     new_idx = 0

     for i in range(N):
         #1을 만났을 때
         if number_list[i] == '1':
            if i != N-1:  #1이면서 마지막값이 아닐때
                one_list.append(i)
            else: #1이면서 마지막 값일 때
                one_list.append(i)
                max_length = max(max_length, len(one_list))
                
         #0을 만났을 때
         else:
             #기존의 최대길이보다 크다면 max_length값 갱신
             if len(one_list) > max_length:
                 max_length = len(one_list)
                 one_list = []  # 초기화
             else:
                 one_list = []  # 초기화
                 continue

     print(f"#{t}", max_length)