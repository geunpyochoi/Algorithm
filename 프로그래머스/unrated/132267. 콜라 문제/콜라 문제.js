function solution(a, b, n) {
    var answer = 0;
    var tmp = 0;
    while (n >= a) {
        tmp += parseInt(n/a) * b;
        n = tmp + (n%a);
        answer += tmp;
        tmp = 0;
    }
    return answer;
}