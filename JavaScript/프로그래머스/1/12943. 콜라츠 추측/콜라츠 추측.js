function solution(num) {
    let i = 0;

    while (i<500) {
        
        if (num === 1) {
            return i
        }
        
        if (num % 2) {
            num = num * 3 + 1;
        } else {
            num = num / 2;
        }
        
        i++;
    }
    
    return -1;
}