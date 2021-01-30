const { strict } = require('assert');

function Main(input) {
    input = input.split('\n');
    const n = Number(input[0]);
    const mem = input[1];
    let min = mem.length;
    let oc = (mem.match(/E/g) || []).length;

    for (let i = 0; i < mem.length; i++) {
        if (mem[i] === 'E') {
            oc--;
        }
        if (mem[i - 1] === 'W') {
            oc++;
        }
        if (min > oc) {
            min = oc;
        }
    }
    console.log(min);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));