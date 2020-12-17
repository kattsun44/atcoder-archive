function Main(input) {
    const [a, b, c] = input.split(' ').map((a, b) => Number(a, b));
    let t = 0;
    let ans = 'NO'

    for (let i = 1; i <= 100; i++) {
        t = a * i % b
        if (t === c) {
            ans = 'YES'
            break;
        }
    }
    console.log(ans);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));