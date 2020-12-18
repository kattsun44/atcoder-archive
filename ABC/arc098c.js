const { strict } = require('assert');

function Main(input) {
    input = input.split('\n');
    const n = Number(input[0]);
    const mem = input[1];
    let min = mem.length;

    for (let i = 0; i < mem.length; i++) {
        const wm = mem.slice(0,i);
        const em = mem.slice(i + 1);
        const oc = (wm.match(/W/g) || []).length +
                   (em.match(/E/g) || []).length;
        if (min > oc) {
            min = oc;
        }
    }
    console.log(min);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));