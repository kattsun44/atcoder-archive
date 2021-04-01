function Main(input) {
    input = input.split('\n').map(a => a.split(' '));
    const n = Number(input[0]);
    const board = input.slice(1, 3);

    let total = 0;       // 各試行回数(n回)ごとの合計
    let array = [];      // 各施行の合計の配列
    let toLower = n - 1; // いつ下の行にいくか
    let nr = 0;          // 今の行

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            total += Number(board[nr][j]);
            if (j === toLower) {
                nr = 1;
                j--;
                toLower--;
            }
        }
        array.push(total);
        total = 0;
        nr = 0;
        
    }
    console.log(Math.max(...array));
}
  
  Main(require('fs').readFileSync('/dev/stdin', 'utf8'));