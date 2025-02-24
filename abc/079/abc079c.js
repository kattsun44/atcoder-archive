function Main(input) {
    input = input.split('').map((a, b) => Number(a,b));
    const [a, b, c, d] = input;
    let [t1, t2, t3] = [0, 0, 0];
    const op = ['+', '-'];
    const ans = [];

    for (let i = 0; i < 2; i++ ) {
        if (i === 0) {
            t1 = a + b;
        } else {
            t1 = a - b;
        }
        for (let j = 0; j < 2; j++) {
            if (j === 0) {
                t2 = t1 + c;
            } else {
                t2 = t1 - c;
            }
            for (let k = 0; k < 2; k++) {
                if (k === 0) {
                    t3 = t2 + d;
                } else {
                    t3 = t2 - d;
                }
                if (t3 === 7) {
                    ans.push(`${a}${op[i]}${b}${op[j]}${c}${op[k]}${d}=7`);
                }
            }
            
        }
    }
    console.log(ans[0]);
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));