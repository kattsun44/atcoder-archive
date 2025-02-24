function Main(input) {
    input = input.split(' ').map((a, b) => Number(a, b));
    const [sx, sy, gx, gy] = input;
    const x = sx + (gx - sx) * sy / (sy + gy);
    console.log(x)
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));