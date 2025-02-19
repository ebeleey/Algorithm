const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./2438.txt";

const n = fs.readFileSync(filePath).toString();

for (let i =1; i<= parseInt(n); i++) {
    console.log("*".repeat(i))
}