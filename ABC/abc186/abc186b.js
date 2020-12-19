function Main(input) {
    input = input.split('\n');
    const [h, w] = input[0].split(' ').map((a, b) => Number(a,b));

    let min = 100;
    let total = 0;

    for (let i = 1; i <= h; i++) {
        row = input[i].split(' ').map((a, b) => Number(a, b));
        const rm = Math.min(...row);
        if (min > rm)  {
            min = rm;
        }
        total += row.reduce((a, c) => {
            return a + c;
        })
    }
    console.log(total - min * h * w);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));