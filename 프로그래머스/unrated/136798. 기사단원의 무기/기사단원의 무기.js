function solution(number, limit, power) {
    const arr = [];
    for(let i = 1; i <= number; i++){
        let n = 0;
        for(let j = 1; j <= Math.sqrt(i); j++){
            if (i / j === j) n += 1;
            else if(i % j === 0) n += 2;
        }
        arr.push(n);
    }
    return arr.map((n) =>{return n > limit ? power : n}).reduce((a,c)=>a+c,0);
}