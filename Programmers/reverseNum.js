//프로그래머스 자연수 뒤집어 배열로 만들기

function solution(n) {
    n = n.toString().split('').reverse();
    for(let i = 0; i < n.length; i++) n[i] = parseInt(n[i]);
    return n;
}
