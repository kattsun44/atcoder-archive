function Main(input) {
    input = input.split('\n');
    const [a, b] = input[0].split(' ').map((a, b) => Number(a, b));
    const [c, d] = input[1].split(' ').map((a, b) => Number(a, b));
    console.log(a * d - b * c);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));