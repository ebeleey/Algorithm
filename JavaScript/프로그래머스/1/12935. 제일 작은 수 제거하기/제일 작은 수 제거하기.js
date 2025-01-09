function solution(arr) {
    let answer = []
    for (item of arr) {
        if (item !== Math.min(...arr)) {
            answer.push(item)
        }
    }
    
    return answer.length ? answer : [-1]
}