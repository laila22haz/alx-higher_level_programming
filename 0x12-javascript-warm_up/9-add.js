#!/usr/bin/node
function add (a, b) {
  const sum = parseInt(a) + parseInt(b);
  console.log(sum);
}
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (!isNaN(arg1) || !isNaN(arg2)) {
  add(arg1, arg2);
} else {
  console.log(NaN);
}
