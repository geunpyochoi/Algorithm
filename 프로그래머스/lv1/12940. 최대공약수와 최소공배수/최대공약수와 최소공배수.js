function solution(n, m) {
    var answer = [];
    let tmp = 0;
    if (n > m){
        tmp = n;
        n = m;
        m = tmp;
    }
    let a = m;
    let b = n;
    let num = 0;
    while (b !== 0){
        num = a%b;
        a = b;
        b = num;
    }
    answer.push(a);
    answer.push((m*n)/a);
    return answer;
}