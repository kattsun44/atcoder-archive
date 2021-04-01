function Main(input) {
    input = input.split('\n').map((a, b) => Number(a,b));
    const n = input[0];
    const log = {};
    let count = 0;

    for (let i = 1; i <= n;) {
        count++;
        const a = input[i];

        // ボタンの数字が「2」の場合、カウント回数を出力
        if (a === 2) {
            console.log(count);
            break;
        // logに今まで押したボタンの番号があれば-1を出力しbreak, なければlogに追加
        } else if (i in log) {
            console.log(-1);
            break;
        } else {
            log[i] = a;
        }
        // 次に押すボタンはa番目
        i = a;
    }
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));