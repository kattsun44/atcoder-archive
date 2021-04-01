function Main(input) {
    input = input.split('\n');
    const [n, m, t] = input[0].split(' ').map((a, b) => Number(a, b));
    let rm = n;
    let [a, b] = [0, 0];

    for (let i = 1; i <= m; i++) {
        a = input[i].split(' ').map((a, b) => Number(a, b))[0];
        rm -= a - b;
        if (rm <= 0) {
            break;
        }
        b = input[i].split(' ').map((a, b) => Number(a, b))[1];
        if (rm + b - a >= n) {
            rm = n;
        } else {
            rm += b -a;
        }
    }

    rm -= t - b;
    if ( rm > 0) {
        console.log('Yes');
    } else {
        console.log('No');
    }
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));