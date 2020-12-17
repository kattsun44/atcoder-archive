function Main(input) {
    const [a, b, c] = input.split(' ').map((a, b) => Number(a, b));
    let t = 0;

    for (let i = 1; i <= 100000; i++) {
        t = a * i % b
        if (t === c) {
            console.log('YES');
            break;
        } else if (i === 100000) {
            console.log('NO');
        }
    }
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));