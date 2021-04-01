function Main(input) {
    input = input.split('\n');
    const [h, w] = input[0].split(' ').map((a, b) => Number(a, b));
    const board = [];
    
    for (let i = 1; i <= h; i++) {
      const row = [];
      for (let j = 0; j < w; j++) {
        row.push(input[i][j]);
      }
      board.push(row);
    }
  
    for (let i = 0; i < h; i++) {
      const pr = board[i - 1] || '.'.repeat(w).split(''); // 1つ前の列
      const cr = board[i];                                // 現在の列
      const nr = board[i + 1] || '.'.repeat(w).split(''); // 次の列
      
      let eight = []; // 周囲8マスの文字の配列
      
      for (let j = 0; j < w; j++) {
        cp = board[i][j]; // 現在の位置
        
        // 現在地が'#'でないとき、'#'の個数を現在位置に代入 
        if (cp !== '#') {
          eight = [pr[j-1], pr[j], pr[j+1],
                   cr[j-1],        cr[j+1],
                   nr[j-1], nr[j], nr[j+1]];
          
          board[i][j] = eight.filter(p => p === '#').length;
        }
      }
      console.log(board[i].join(''));
    }
    
  }
  
  Main(require('fs').readFileSync('/dev/stdin', 'utf8'));