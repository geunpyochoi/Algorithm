function solution(n) {
    n = n.toString().split('').sort().reverse();
    let answer = ''
    for(i = 0; i < n.length; i++) answer += n[i];
    return +answer;
}