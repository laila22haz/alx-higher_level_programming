#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
	  if (w > 0 && h > 0) {
		this.width = w;
		this.height = h;
    }
  }
  print() {
	for (let index = 0; index < this.height; index++) {
		let rect = '';
		for (let j = 0; j < this.width; j++) {
			rect += 'X';
		}
		console.log(rect);
	}
  }
}
module.exports = Rectangle;
