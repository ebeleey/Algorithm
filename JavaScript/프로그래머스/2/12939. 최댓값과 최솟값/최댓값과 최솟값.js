function solution(s) {    
    let nums = s.split(" ").map(x => parseInt(x));
    return String(Math.min(...nums)) + " " + String(Math.max(...nums));
}