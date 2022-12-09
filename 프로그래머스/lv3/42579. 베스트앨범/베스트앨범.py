def solution(genres, plays):
    genres_total_count = {}
    genres_each = {}
    
    # 플레이 리스트를 만들도록 기준별로 정리
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        # 1. 각 장르별로 총 조회수를 genres_total_count로 정리
        # 2. 각 장르별 고유번호, 조회수별로 정리
        if genre not in genres_total_count:
            genres_total_count[genre] = play 
            genres_each[genre] = [[idx, play]]
        else:
            genres_total_count[genre] += play
            genres_each[genre].append([idx, play])
    
    # 정렬
    # 1. 조회수를 기준으로 내림차수 정렬
    genres_total_count = dict(sorted(genres_total_count.items(), key=lambda x: x[1], reverse=True))
    # 2. 개별 장르별 조회수 기준으로 내림차수 정렬
    for each in genres_each.values():
        each.sort(key=lambda x: (-x[1], x[0]))
    
    # 삽입
    answer = []
    for key in genres_total_count.keys():
        answer.append(genres_each[key][0][0])
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
        if len(genres_each[key]) >=2:
            answer.append(genres_each[key][1][0])

    return answer