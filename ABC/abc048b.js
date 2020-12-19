function Main(input) {
    input = input.split(' ').map((a, b) => Number(a, b));
    const [a, b, x] = input;
    let total = 0;

    total += Math.floor((b - a) / x);
    if (a % x === 0) {
        total++;
    }
    console.log(Number(total));
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));