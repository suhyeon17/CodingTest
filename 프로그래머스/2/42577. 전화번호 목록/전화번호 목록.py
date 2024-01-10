def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        pre = phone_book[i]
        len_pre = len(pre)
        if phone_book[i+1][:len_pre] == pre:
            return False
    
    return True