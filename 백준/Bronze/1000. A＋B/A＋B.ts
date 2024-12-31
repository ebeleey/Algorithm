const rl = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', (input) => {
  const [A, B] = input.split(' ').map(Number);
  console.log(A + B);
  rl.close();
});
