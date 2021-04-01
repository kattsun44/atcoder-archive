function Main(input) {
    input = input.split('\n');
    const [n, x] = input[0].split(' ').map((a, b) => Number(a, b));
    let ans = x;

    for (let i = 0; i < n; i++) {
        const jd = input[1][i];
        if (ans > 0 && jd === 'x') {
            ans--;
        } else if (jd === 'o') {
            ans++;
        }
    }
    console.log(ans);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));