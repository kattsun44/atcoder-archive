function Main(input) {
    input = input.split('\n');
    const [h, w] = input[0].split(' ').map((a, b) => Number(a, b));
    const board = [];
    
    // キャンバス(board)作成
    for (let i = 1; i <= h; i++) {
      let row = [];
      for (let j = 0; j < w; j++) {
        row.push(input[i][j]);
      }
      board.push(row);
    }
    
    // 塗れないかどうか
    let no = false;
    
    for (let i = 0; i < h; i++) {
      // 1つ前、現在、次の行
      const ub = board[i - 1] || '.'.repeat(w).split('');
      const cb = board[i];
      const lb = board[i + 1] || '.'.repeat(w).split('');
      
      for (let j = 0; j < w; j++) {
        // 今のマスが'#'の時、上下左右に'#'が無ければno=true
        const pos = board[i][j];
        const crossGrids = [];
        if (pos === '#') {
          crossGrids.push(ub[j], cb[j + 1], lb[j], cb[j - 1]);
          if (crossGrids.indexOf('#') === -1) {
            no = true;
            break;
          }
        }
      }
      if (no) {
        console.log('No');
        break;
      } else if (i === h - 1) {
        console.log('Yes');
      }
    }
  }
  
  Main(require('fs').readFileSync('/dev/stdin', 'utf8'));