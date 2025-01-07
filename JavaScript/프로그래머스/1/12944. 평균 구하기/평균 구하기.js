function solution(arr) {
    var answer = 0;
    for (num of arr) {
        answer += num;
    }
    answer = answer / arr.length;
    return answer;
}