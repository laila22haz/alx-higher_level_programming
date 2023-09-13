#!/usr/bin/node
const argv = process.argv.length;

if (argv <= 3) {
  console.log('0');
} else {
  const n = process.argv.slice(2).map(Number);
  const second = n.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
