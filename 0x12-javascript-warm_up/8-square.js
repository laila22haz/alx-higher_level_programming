#!/usr/bin/node
const size = parseInt(process.argv[2]);
let row;
if ((size)) {
  for (let i = 0; i < size; i++) {
    row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
