function solution(n) {
    return n % Math.sqrt(n) ? -1 : Math.pow(Math.sqrt(n)+1, 2)
}