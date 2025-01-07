function solution(n) {  
    let arr = [];
    while(n > 0) {
        arr.push(n%10);
        n = Math.floor(n/10);
    }
    
    arr.sort().reverse();
    return parseInt(arr.join(''));
}