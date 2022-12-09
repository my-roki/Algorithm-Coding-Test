def solution(genres, plays):
    genres_total_count = {}
    genres_each = {}
    
    # 정리
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genres_total_count:
            genres_total_count[genre] = play 
            genres_each[genre] = [[idx, play]]
        else:
            genres_total_count[genre] += play
            genres_each[genre].append([idx, play])
    
    # 정렬
    genres_total_count = dict(sorted(genres_total_count.items(), key=lambda x: x[1], reverse=True))
    for each in genres_each.values():
        each.sort(key=lambda x: (-x[1], x[0]))
    
    # 삽입
    answer = []
    for key in genres_total_count.keys():
        answer.append(genres_each[key][0][0])
        if len(genres_each[key]) >=2:
            answer.append(genres_each[key][1][0])

        
    return answer