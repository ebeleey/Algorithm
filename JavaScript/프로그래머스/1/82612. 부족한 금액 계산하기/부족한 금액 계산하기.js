function solution(price, money, count) {
    var answer = money;
    
    for (let i=1; i<count+1; i++) {
        answer -= price*i;
    }

    return answer >= 0 ? 0 : -answer
}