#!/usr/bin/node
const myconst = 'is';
if (process.argv[2] || process.argv[3]) {
  console.log(process.argv[2] + ' ' + myconst + ' ' + process.argv[3]);
} else {
  console.log('undefined' + ' ' + myconst + ' ' + 'undefined');
}
