function Main(input) {
    const n = Number(input);
    let p = 1;
  
    for (let i = 1; i <= n; i++) {
      p = p * i % 1000000007;
    }
    console.log(p);
  }
  
  Main(require('fs').readFileSync('/dev/stdin', 'utf8'));