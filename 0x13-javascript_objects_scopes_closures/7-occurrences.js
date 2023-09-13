#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const occure of list) {
    if (occure === searchElement) {
      counter++;
    }
  }
  return counter;
};
