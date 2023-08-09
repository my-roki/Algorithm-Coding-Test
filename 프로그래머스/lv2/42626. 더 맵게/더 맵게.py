import heapq

def solution(scoville:list, K:int):
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K and len(scoville) > 1: 
        lowest_scoville1 = heapq.heappop(scoville)
        lowest_scoville2 = heapq.heappop(scoville)

        new_scoville = lowest_scoville1 + (lowest_scoville2 * 2)
        heapq.heappush(scoville, new_scoville)

        answer += 1
    
    return answer if scoville[0] >= K else -1