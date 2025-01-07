function solution(s){
    
    let pCnt = 0;
    let yCnt = 0;
    
    for (char of s) {
        if (char === 'p' || char === 'P') {
            pCnt += 1;
        } else if (char === 'y' || char === 'Y') {
            yCnt += 1;
        }
    }
    
    console.log(pCnt, yCnt)

    return pCnt === yCnt;
}