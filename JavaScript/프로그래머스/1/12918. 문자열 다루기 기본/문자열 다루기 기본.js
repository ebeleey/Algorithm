function solution(s) {
    for (char of s) {
        if (isNaN(char)) {
            return false;
        }
    }
    return s.length === 4 || s.length === 6 ? true : false;
}

console.log(solution("0x16"))