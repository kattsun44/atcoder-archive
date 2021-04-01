function Main(input) {
    input = input.split(' ').map((a, b) => Number(a, b));
    const [a, b, c, d] = input;
  
    let s = Math.min(b, d) - Math.max(a, c);
    if (s <= 0) {s = 0;}
    console.log(s);
  }
  
  Main(require('fs').readFileSync('/dev/stdin', 'utf8'));