function solution(arr, divisor) {
    let answer = []
    for (item of arr) {
        if (!Boolean(item % divisor)) {
            answer.push(item)
        } 
    }
    if (answer.length === 0) {
        answer.push(-1)
    } else {
        answer.sort((a, b) => a - b)
    }
    return answer
}