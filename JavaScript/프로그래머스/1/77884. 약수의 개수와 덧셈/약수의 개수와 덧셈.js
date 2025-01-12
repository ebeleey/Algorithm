function solution(left, right) {
    var answer = 0;
    
    for (let num=left; num<right+1; num++) {
        let cnt = 0;
        
        if (num === 1) {
            cnt = 1;    
        } else {
            cnt = 0;
            for (let i=2; i<num/2+1; i++) {
                if (num%i===0) {
                    cnt++;
                } 
            }
        }    
        if (cnt%2) {
            //약수의 개수가 홀수면
            answer -= num;
        } else {
            //약수의 개수가 짝수면 
            answer += num;
      }
    }
    return answer;
}