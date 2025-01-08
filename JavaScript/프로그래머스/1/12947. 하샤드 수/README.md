# [level 1] 하샤드 수 - 12947 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12947) 

### 성능 요약

메모리: 33.4 MB, 시간: 0.08 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 08일 23:25:18

### 문제 설명

<p>양의 정수 <code>x</code>가 하샤드 수이려면 <code>x</code>의 자릿수의 합으로 <code>x</code>가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 <code>x</code>를 입력받아 <code>x</code>가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.</p>

<h5>제한 조건</h5>

<ul>
<li><code>x</code>는 1 이상, 10000 이하인 정수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>x</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td style="text-align: center">true</td>
</tr>
<tr>
<td>12</td>
<td style="text-align: center">true</td>
</tr>
<tr>
<td>11</td>
<td style="text-align: center">false</td>
</tr>
<tr>
<td>13</td>
<td style="text-align: center">false</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong><br>
10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.</p>

<p><strong>입출력 예 #2</strong><br>
12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.</p>

<p><strong>입출력 예 #3</strong><br>
11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.</p>

<p><strong>입출력 예 #4</strong><br>
13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.</p>

<hr>

<p>※ 공지 - 2023년 5월 27일 문제 지문 오탈자 수정되었습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## `reduce()` 사용법
```js
  arr.reduce(callback[, initialValue])
```

- `callback`: 배열의 각 요소에 대해 실행할 함수
  - `accumulator`: 콜백 함수의 반환값을 누적하는 변수 
  - `currentValue` : 현재 처리 중인 배열 요소
  - `currentIndex` : 현재 처리 중인 배열 요소의 인덱스(optional)
  - `array` : `reduce()`가 호출된 배열(optional)
- `initialValue`: 콜백 함수의 최초 호출에 제공할 초기값

> 콜백의 최초 호출 때 `accumulator`와 `currentValue`는 다음 두 가지 값 중 하나를 가질 수 있습니다. 만약 `reduce()` 함수 호출에서 `initialValue`를 제공한 경우, `accumulator`는 `initialValue`와 같고 `currentValue`는 배열의 첫 번째 값과 같습니다. `initialValue`를 제공하지 않았다면, `accumulator`는 배열의 첫 번째 값과 같고 `currentValue`는 두 번째와 같습니다.

## 초기값 0을 설정하지 않았을 때 정답이 아니었던 이유??

### 초기값이 없을 때
```js
String(x).split('').reduce((acc, cur) => acc + Number(cur))
```

- `x`가 `18`이면 `String(x).split('')을 수행한 배열은 `['1', '8']`
- `initialValue`를 제공하지 않으면 배열의 첫 번째 값이 초기값이 됨.
- 첫 번째 연산은 `acc`이 `'1'`이고 `cur`은 `'8'`이 되어서 `'1' + Number('8')`이 수행되어 `'18'`이 됨.

자릿수 합 계산이 이루어지지 않음.

### 초기값을 0으로 설정했을 때
```js
String(x).split('').reduce((acc, cur) => acc + Number(cur), 0)
```
1. `acc=0`, `cur='1'` -> `acc+Number(cur)` = `0+1` = `1`
2. `acc=1`, `cur='8'` -> `acc+Number(cur)` = `1+8` = `9`

자릿수 합 계산이 제대로 이루어진다!!
