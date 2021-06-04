def hotel(arrive, depart, K):
    if len(arrive) != len(depart):
        return None
    n = len(arrive)
    arrive.sort()
    depart.sort()
    count = 0
    i = 0
    j = 0
    while (i < n and j < n):
        if arrive[i] < depart[j]:
            i += 1
            count += 1
            if count > K:
                return False
        else:
            j += 1
            count -= 1
    return True





arrival = [1,3,5]
departures = [2,6,8]
K=1
print(hotel(arrival,departures,K))