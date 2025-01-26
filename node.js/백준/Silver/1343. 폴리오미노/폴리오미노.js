// 폴리오미노
// 문자열 치환하는 replace() 함수

const fs = require("fs");
const filePath = process.platform === "linux" ? "dev/stdin" : "./input.txt";

const input = fs.readFileSync(filePath).toString().trim();

let answer = ''
answer = input.replace(/XXXX/g, 'AAAA').replace(/XX/g, 'BB');

console.log(answer.split('').includes('X') ? -1 : answer)