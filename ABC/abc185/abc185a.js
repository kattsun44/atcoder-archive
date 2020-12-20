function Main(input) {
    input = input.split(' ').map((a, b) => Number(a, b));
    const qs = input;
    console.log(Math.min(...qs))
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));