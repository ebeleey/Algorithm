const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const stack = [];
const result = [];

const N = parseInt(input[0]);

for (let i = 1; i <= N; i++) {
    const [command, value] = input[i].split(" ");
    
    switch (command) {
        case "push":
            stack.push(parseInt(value));
            break;
        case "pop":
            result.push(stack.length ? stack.pop() : -1);
            break;
        case "size":
            result.push(stack.length);
            break;
        case "empty":
            result.push(stack.length ? 0 : 1);
            break;
        case "top":
            result.push(stack.length ? stack[stack.length-1] : -1);
            break;
    }
}

console.log(result.join("\n"));