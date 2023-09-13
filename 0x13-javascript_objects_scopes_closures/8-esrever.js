#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let index = list.length - 1; index > -1; index--) {
    newlist.push(list[index]);
  }
  return newlist;
};
