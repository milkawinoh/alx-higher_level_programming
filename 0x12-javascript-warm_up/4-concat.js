#!/usr/bin/node
let string = "is"
let argument = process.argv[2].concat(" ",string, " ", process.argv[3])

console.log(argument)