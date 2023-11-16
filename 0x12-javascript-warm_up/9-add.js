#!/usr/bin/node
let a = process.argv[2];
let b = process.argv[3];
function add(a, b)
{
    console.log(parseInt(a) + parseInt(b))
}
add(a,b)
