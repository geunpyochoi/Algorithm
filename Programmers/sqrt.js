// 프로그래머스 정수 제곱근 판별

function solution(n) {
    return Number.isInteger(Math.sqrt(n)) ? (Math.sqrt(n)+1)*(Math.sqrt(n)+1) : -1;
}
