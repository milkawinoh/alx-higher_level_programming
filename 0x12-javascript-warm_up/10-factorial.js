#!/usr/bin/node

function factorial(x) {
    if (isNaN(x) || x < 0) {
        return 1;
    } else if (x === 0 || x === 1) {
        return 1;
    } else {
        return x * factorial(x - 1);
    }
}

let a = parseInt(process.argv[2]);

console.log(factorial(a));
