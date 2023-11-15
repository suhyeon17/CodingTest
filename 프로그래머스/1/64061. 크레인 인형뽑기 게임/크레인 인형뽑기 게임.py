def solution(board, moves):
    answer = 0
    basket, idx = [], -1
    n = len(board)
    
    for m in moves:
        #바구니에 인형 담기
        for i in range(n):
            if board[i][m-1] != 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                idx += 1
                break
        #바구니 확인
        if len(basket) >= 2:
            if basket[idx] == basket[idx-1]:
                basket.pop()
                basket.pop()
                idx -= 2
                answer += 2
        
    return answer
                