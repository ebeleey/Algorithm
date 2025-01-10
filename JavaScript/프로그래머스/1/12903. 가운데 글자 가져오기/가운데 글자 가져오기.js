function solution(s) {
    if (s.length % 2) {
        return s.slice(Math.floor(s.length/2), Math.floor(s.length/2)+1)
    } else {
        return s.slice(Math.floor(s.length/2)-1, Math.floor(s.length/2)+1)
    }
}