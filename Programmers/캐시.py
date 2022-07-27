# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램

# 캐시 크기, 도시이름 배열
import collections


def solution(cacheSize, cities):
    if cacheSize <= 0:
        return len(cities) * 5

    cache = collections.deque([])
    t = 0
    for city in cities:
        city = city.lower()
        # cache miss
        if city not in cache:
            # 큐가 꽉 찼다면
            if len(cache) >= cacheSize:
                # 최근에 사용하지 않은 아이를 제거해야 함
                cache.popleft()
            t += 5
        # cache hit
        else:
            cache.remove(city)
            t += 1
        cache.append(city)
    return t


cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize = 5
print(solution(cacheSize, cities))
