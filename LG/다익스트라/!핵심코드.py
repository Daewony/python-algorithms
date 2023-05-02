disk[K] = 0  # 거리배열 초기화
heapq.heappush(heap, (0, K))  # K는 시작점

while heap:  # heap이 떨어질때까지 반복
    w, v = heapq.heappop(heap)  # w: 현재비용, v:현재노드
    if w != dist[v]:
        continue  # 최솟값만 진행?
    for nw, nv in edge[v]:  # 인접리스트에서 다음 간선비용, 노드값을 뽑아서
        if dist[nv] > dist[v]+nw:  # 현재 관리 거리 배열이 너 크면
            dist[nv] = dist[v]+nw  # 갱신
            heapq.heappush(heap, (dist[nv], nv))  # 힙에 넣기
