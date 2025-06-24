function calculate(r, w) {
    return Math.sqrt(r ** 2 - w ** 2);
}

function solution(r1, r2) {
    let answer = 0;
    
    for (let w = 1; w < r2; w++) {
        const h1 = calculate(r1, w);
        const h2 = calculate(r2, w);
        
        if (w >= r1) {
            answer += Math.floor(h2) + 1;
            continue;
        }
        
        answer += Math.floor(h2) - Math.floor(h1);
        
        if (Number.isInteger(h1)) {
            answer += 1;
        }
    }
    
    return 4 * (answer + 1);
}