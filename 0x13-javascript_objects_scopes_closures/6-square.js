#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    for (let index = 0; index < this.height; index++) {
      let rect = '';
      for (let j = 0; j < this.width; j++) {
        rect += c || 'X';
      }
      console.log(rect);
    }
  }
}
module.exports = Square;
