function solution(n) {
    n = n.toString().split('').reverse();
    for(let i = 0; i < n.length; i++) n[i] = parseInt(n[i]);
    return n;
}