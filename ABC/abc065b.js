function Main(input) {
    input = input.split('\n').map((a, b) => Number(a,b));
    const n = input[0];
    const log = [1];
    let count = 0;

    for (let i = 1; i <= n;) {
        count++;
        a = input[i];

        // ボタンの数字が「2」の場合、カウント回数を出力
        if (a === 2) {
            console.log(count);
            break;
        // a=1 or logに今まで押したボタンの番号があればbreak、なければlogに追加
        } else if (a === 1 || log.indexOf(a) !== -1) {
            console.log(-1);
            break;
        } else {
            log.push(a);
        }
        // 次に押すボタンはa番目
        i = a;
    }
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));