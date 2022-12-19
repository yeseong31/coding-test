# [level 4] 무지의 먹방 라이브 - 42891 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42891?language=python3) 

### 성능 요약

메모리: 43.5 MB, 시간: 143.22 ms

### 구분

코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT

### 채점결과

<br/>정확성: 42.9<br/>효율성: 57.1<br/>합계: 100.0 / 100.0

### 문제 설명

<h2>무지의 먹방 라이브</h2>

<p><code>* 효율성 테스트에 부분 점수가 있는 문제입니다.</code></p>

<p>평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어 졌고 고민 끝에 카카오 TV 라이브로 방송을 하기로 마음먹었다.</p>

<p><img src="https://grepp-programmers.s3.amazonaws.com/files/production/10f4f72c93/1d932bfc-8082-4b7e-b30d-ab46bf71a9f2.png" title="" alt="muji_live.png"></p>

<p>그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다. </p>

<p>회전판에 먹어야 할 N 개의 음식이 있다. <br>
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다. <br>
무지는 다음과 같은 방법으로 음식을 섭취한다.</p>

<ul>
<li>무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.</li>
<li>마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.</li>
<li>무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.

<ul>
<li>다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.</li>
</ul></li>
<li>회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.</li>
</ul>

<p>무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.<br>
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다. <br>
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.</p>

<h5>제한사항</h5>

<ul>
<li>food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열이다.</li>
<li>k 는 방송이 중단된 시간을 나타낸다.</li>
<li>만약 더 섭취해야 할 음식이 없다면 <code>-1</code>을 반환하면 된다.</li>
</ul>

<h5>정확성 테스트 제한 사항</h5>

<ul>
<li>food_times 의 길이는 <code>1</code> 이상 <code>2,000</code> 이하이다.</li>
<li>food_times 의 원소는 <code>1</code> 이상 <code>1,000</code> 이하의 자연수이다.</li>
<li>k는 <code>1</code> 이상 <code>2,000,000</code> 이하의 자연수이다.</li>
</ul>

<h5>효율성 테스트 제한 사항</h5>

<ul>
<li>food_times 의 길이는 <code>1</code> 이상 <code>200,000</code> 이하이다.</li>
<li>food_times 의 원소는 <code>1</code> 이상 <code>100,000,000</code> 이하의 자연수이다.</li>
<li>k는 <code>1</code> 이상 <code>2 x  10^13</code> 이하의 자연수이다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>food_times</th>
<th>k</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[3, 1, 2]</td>
<td>5</td>
<td>1</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>0~1초 동안에 1번 음식을 섭취한다. 남은 시간은 [2,1,2] 이다.</li>
<li>1~2초 동안 2번 음식을 섭취한다. 남은 시간은 [2,0,2] 이다.</li>
<li>2~3초 동안 3번 음식을 섭취한다. 남은 시간은 [2,0,1] 이다.</li>
<li>3~4초 동안 1번 음식을 섭취한다. 남은 시간은 [1,0,1] 이다.</li>
<li>4~5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은 [1,0,0] 이다.</li>
<li>5초에서 네트워크 장애가 발생했다. 1번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에 1번 음식부터 다시 먹기 시작하면 된다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

### 문제 풀이
- 처음에는 deque()를 이용하여 순서대로 음식을 섭취하는 것을 반복하였는데, 제한 시간을 초과하여 효율성에서 통과하지 못했다.
  ```python
  # 효율성에서 떨어진 코드
  from collections import deque


  def solution(food_times, k):
      q = deque([(i, v) for i, v in enumerate(food_times, 1)])
      for _ in range(k):
          idx, food = q.popleft()
          food -= 1
          if food != 0:
              q.append((idx, food))
        
      return q.popleft()[0]
  ```
  - food_times와 k가 각각 200000, 2000000까지 될 수 있으므로 단순 for문을 도는 것만으로도 제한 시간을 초과한다.


- 따라서 섭취할 때 **시간이 적게 걸리는 음식부터 제거해 나가는 방법**으로 문제를 해결하였다.


- 먼저 섭취 시간이 짧은 순으로 우선순위 큐를 설정한다.
  ```python
  q = [(v, i) for i, v in enumerate(food_times, 1)]
  heapify(q)
  ```

  - 우선순위 큐를 이용하여 섭취 시간을 구하는 공식은 다음과 같다.
  > 섭취 시간 
  >
  > = (현재 음식 섭취 시간 - 이전 음식 섭취 시간) x 남은 음식의 수
  > 
  > = (heappop(q)[0] - prev) * length

    - 이전 음식 섭취 시간을 계산 과정에서 빼는 이유는 다음과 같다.
      - 음식 섭취 과정에서 회전판이 음식 섭취 시간만큼 회전한다.
      - 이때 회전 횟수만큼 나머지 음식들도 양이 줄어든다.
      - 즉 현재 음식은 이미 이전 음식의 섭취 시간만큼 섭취된 상태이므로 이를 반영하여 계산을 수행해야 한다.

- 이 공식을 코드로 최종 적용하면 다음과 같다.
  ```python
  while q and (q[0][0] - prev) * len(q) <= k:
      t = heappop(q)[0]
      k -= (t - prev) * (len(q) + 1)  # heappop으로 인해 len(q)는 1이 작은 상태임
      prev = t
  ```

- 반복문을 빠져나오는 시점의 k는 무지 기준으로 회전판을 돌려가며 남은 음식을 먹어야 할 횟수(초)가 된다.
- 따라서 heapify 시킨 q를 다시 음식 번호 순으로 정렬시킨 후 나머지 연산으로 최종 결과를 선택 후 이를 반환하면 된다.
  ```python
  return sorted(q, key=lambda x: x[1])[k % len(q)][1]
  ```
  
- 최종 코드는 [이곳](https://github.com/yeseong31/COTE/blob/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/lv4/42891.%E2%80%85%EB%AC%B4%EC%A7%80%EC%9D%98%E2%80%85%EB%A8%B9%EB%B0%A9%E2%80%85%EB%9D%BC%EC%9D%B4%EB%B8%8C/%EB%AC%B4%EC%A7%80%EC%9D%98%E2%80%85%EB%A8%B9%EB%B0%A9%E2%80%85%EB%9D%BC%EC%9D%B4%EB%B8%8C.py)을 참고한다.
