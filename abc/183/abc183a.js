function Main(input) {
    input = Number(input);
    if (input >= 0) {
        console.log(input);
    } else {
        console.log(0);
    }
}

Main(require('fs').readFileSync('/dev/stdin', 'utf8'));