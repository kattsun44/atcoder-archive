function Main(input) {
    input = input.split(' ').map((a, b) => Number(a,b));
    const [n, w] = input;
    console.log(Math.floor(n / w));
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));