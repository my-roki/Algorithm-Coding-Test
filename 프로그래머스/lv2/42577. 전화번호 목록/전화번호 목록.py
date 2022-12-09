def solution(phone_book):
    dict = {}
    for phone_number in phone_book:
        dict[phone_number] = phone_number
    
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dict and temp != phone_number:
                return False
    return True
    
