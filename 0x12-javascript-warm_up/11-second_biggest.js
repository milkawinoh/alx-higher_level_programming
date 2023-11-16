#!/usr/bin/node

if (process.argv.length <= 3) {
    console.log(0);
} else {
    let max = parseInt(process.argv[2]);
    let secondMax = parseInt(process.argv[2]);

    for (let i = 3; i < process.argv.length; i++) {
        let current = parseInt(process.argv[i]);

        if (!isNaN(current)) {
            if (current > max) {
                secondMax = max;
                max = current;
            } else if (current > secondMax && current < max) {
                secondMax = current;
            }
        }
    }

    console.log(secondMax);
}
