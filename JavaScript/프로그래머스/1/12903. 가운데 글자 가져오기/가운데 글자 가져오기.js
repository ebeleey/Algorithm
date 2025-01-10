function solution(s) {
    const length = s.length 
    const middle = Math.floor(s.length / 2);
    
    if (length % 2 === 0) {
        return s.slice(middle - 1, middle + 1);
    } else {
        return s[middle];
    }
}