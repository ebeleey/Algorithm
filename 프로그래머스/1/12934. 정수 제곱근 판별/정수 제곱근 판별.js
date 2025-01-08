function solution(n) {
    const sqrt_n = Math.sqrt(n);
    if (sqrt_n - Math.floor(sqrt_n)) {
        return -1
    } else {
        return Math.pow(sqrt_n+1, 2);
    }
}