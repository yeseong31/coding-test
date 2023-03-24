# [unrated] [PCCP 모의고사 #1] 체육대회 - 121684 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/121684) 

### 성능 요약

메모리: 10.2 MB, 시간: 68.43 ms

### 구분

프로그래밍 강의 > PCCP 모의고사 1회

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>당신이 다니는 학교는 매년 체육대회를 합니다. 체육대회는 여러 종목에 대해 각 반의 해당 종목 대표가 1명씩 나와 대결을 하며, 한 학생은 최대 한개의 종목 대표만 할 수 있습니다. 당신의 반에서도 한 종목당 1명의 대표를 뽑으려고 합니다. 학생들마다 각 종목에 대한 능력이 다르지만 이 능력은 수치화되어 있어 미리 알 수 있습니다. 당신의 반의 전략은 각 종목 대표의 해당 종목에 대한 능력치의 합을 최대화하는 것입니다.</p>

<p>다음은 당신의 반 학생이 5명이고, 종목의 개수가 3개이며, 각 종목에 대한 학생들의 능력치가 아래 표와 같을 때, 각 종목의 대표를 뽑는 예시입니다.</p>
<table class="table">
        <thead><tr>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
        <tbody><tr>
<td></td>
<td>테니스</td>
<td>탁구</td>
<td>수영</td>
</tr>
<tr>
<td>석환</td>
<td>40</td>
<td>10</td>
<td>10</td>
</tr>
<tr>
<td>영재</td>
<td>20</td>
<td>5</td>
<td>0</td>
</tr>
<tr>
<td>인용</td>
<td>30</td>
<td>30</td>
<td>30</td>
</tr>
<tr>
<td>정현</td>
<td>70</td>
<td>0</td>
<td>70</td>
</tr>
<tr>
<td>준모</td>
<td>100</td>
<td>100</td>
<td>100</td>
</tr>
</tbody>
      </table>
<p>테니스 대표로 준모, 탁구 대표로 인용, 수영 대표로 정현을 뽑는다면, 세 명의 각 종목에 대한 능력치의 합은 200(=100+30+70)이 됩니다. <br>
하지만, 테니스 대표로 석환, 탁구 대표로 준모, 수영 대표로 정현을 뽑는다면 세 명의 각 종목에 대한 능력치 합은 210(=40+100+70)이 됩니다. 이 경우가 당신의 반의 각 종목 대표의 능력치 합이 최대가 되는 경우입니다.</p>

<p>당신의 반 학생들의 각 종목에 대한 능력치를 나타내는 2차원 정수 배열 <code>ability</code>가 주어졌을 때, 선발된 대표들의 해당 종목에 대한 능력치 합의 최대값을 return 하는 solution 함수를 완성하시오.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>ability</code>의 행의 길이 = 학생 수 ≤ 10</li>
<li>1 ≤ <code>ability</code>의 열의 길이 = 종목 수 ≤ <code>ability</code>의 행의 길이</li>
<li>0 ≤ <code>ability[i][j]</code> ≤ 10,000

<ul>
<li><code>ability[i][j]</code>는 <code>i+1</code>번 학생의 <code>j+1</code>번 종목에 대한 능력치를 의미합니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>ability</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>[[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]</td>
<td>210</td>
</tr>
<tr>
<td>[[20, 30], [30, 20], [20, 30]]</td>
<td>60</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>1번 학생이 2번 종목을, 2번 학생이 1번 종목의 대표로 참가하는 경우에 대표들의 해당 종목에 대한 능력치의 합이 최대가 되며, 이는 60입니다.</li>
</ul>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges