def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {i : 0 for i in id_list}

    report = list(set(report))
    for usr in report:
        a, b = usr.split(" ")
        reported[b] += 1
        
    for usr in report:
        a, b = usr.split(" ")
        if reported[b] >= k:
            answer[id_list.index(a)] += 1
            
            

                
    
    return answer