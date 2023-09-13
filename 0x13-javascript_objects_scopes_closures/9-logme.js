#!/usr/bin/node
let arg = 0;
exports.logMe = function (item) {
  console.log(arg + ': ' + item);
  arg++;
};
