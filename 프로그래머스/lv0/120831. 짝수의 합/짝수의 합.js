function solution(n) {
    var answer = 0;
    return Array(n).fill(0).map((_,i)=> i+1).filter(v => v%2 === 0).reduce((a,c)=>a+c,0);
}