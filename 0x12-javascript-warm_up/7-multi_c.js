#!/usr/bin/node
const number = process.argv[2];
let index = 0;
if (number) {
  while (index < number) {
    console.log('C is fun');
    index += 1;
  }
} else {
  console.log('Missing number of occurrences');
}
