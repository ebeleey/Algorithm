# [level 1] 나누어 떨어지는 숫자 배열 - 12910 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12910) 

### 성능 요약

메모리: 39.4 MB, 시간: 4.66 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 01월 09일 09:41:25

### 문제 설명

<p>array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.<br>
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요. </p>

<h5>제한사항</h5>

<ul>
<li>arr은 자연수를 담은 배열입니다.</li>
<li>정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.</li>
<li>divisor는 자연수입니다.</li>
<li>array는 길이 1 이상인 배열입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>arr</th>
<th>divisor</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[5, 9, 7, 10]</td>
<td>5</td>
<td>[5, 10]</td>
</tr>
<tr>
<td>[2, 36, 1, 3]</td>
<td>1</td>
<td>[1, 2, 3, 36]</td>
</tr>
<tr>
<td>[3,2,6]</td>
<td>10</td>
<td>[-1]</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예#1<br>
arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.</p>

<p>입출력 예#2<br>
arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.</p>

<p>입출력 예#3<br>
3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

---

## 숫자 배열 정렬하기

Javascript에서 배열을 정렬할 때 `arr.sort()`를 사용하면 배열의 요소들이 문자열로 변환되어 정렬됨. 따라서 숫자 배열은 제대로 정렬되지 않음.

`arr.sort()` 메서드는 비교 함수를 사용하여 배열의 요소들을 두 개씩 비교하면서 정렬을 진행한다.
그 때 두 요소를 비교하는 임시 변수를 `a`와 `b`라고 한다.

### 오름차순 정렬

```js
answer.sort((a,b) => a-b)
```

`a-b` 방식은 두 값의 차이를 기준으로 그 순서를 결정하는 방법이다.
- `a-b<0` : `a`가 `b`보다 작은 경우 `a`가 앞에 온다.
- `a-b>0` : `a`가 `b`보다 큰 경우 `b`가 앞에 온다.
- `a-b===0` : `a`와 `b`가 같으면 순서가 바뀌지 않는다.

따라서 `arr.sort((a,b) => a-b)`를 사용하면 두 숫자 `a`와 `b`를 실제 숫자 값으로 비교하여 올바르게 오름차순 정렬을 할 수 있음.


### 내림차순 정렬
```js
arr.sort((a,b) => b-a)
```

### 객체 배열에서 특정 조건을 기준으로 정렬
```js
const students = [
    { name: 'John', score: 85 },
    { name: 'Jane', score: 92 },
    { name: 'Alice', score: 78 },
    { name: 'Bob', score: 88 }
];

// 점수를 기준으로 오름차순 정렬
students.sort((a, b) => a.score - b.score);
console.log(students);  
// [ { name: 'Alice', score: 78 }, { name: 'John', score: 85 }, { name: 'Bob', score: 88 }, { name: 'Jane', score: 92 }]
```

## 다른 사람 코드

```js
function solution(arr, divisor) {
    var answer = arr.filter(v => v%divisor == 0);
    return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}
```
### 배열 필터링(`filter`)
```js
arr.filter(v => v % divisor == 0)
```
배열 arr의 요소 중 divisor로 나누어 떨어지는 요소만을 선택하여 새로운 배열을 만든다.

### 빈 배열 확인
삼항연산자를 사용하여 간단하게 체크
