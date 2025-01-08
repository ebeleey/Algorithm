function solution(x) {
    return !Boolean(x%String(x).split('').reduce((acc, cur)=> acc + Number(cur), 0))
}