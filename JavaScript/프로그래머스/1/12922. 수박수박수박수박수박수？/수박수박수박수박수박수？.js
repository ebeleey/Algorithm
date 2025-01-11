function solution(n) {
    let answer = ""
    for (let i=0; i<parseInt(n/2); i++) {
        answer += "수박"
    }
    if (n % 2) { // 홀수
        answer += "수"
    }
    return answer
}