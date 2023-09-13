#!/usr/bin/node
const number = process.argv[2];
function factorial (number) {
  if (isNaN(number) || number < 0) {
    return 1;
  } else if (number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(number));
