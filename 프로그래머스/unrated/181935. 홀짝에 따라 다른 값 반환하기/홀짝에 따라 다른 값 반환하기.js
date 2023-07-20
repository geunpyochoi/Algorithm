function solution(n) {
    var answer = 0;
    if (n % 2 == 1){
        for(i = 1; i <= n; i++){
            answer += i;
            i += 1
        }
    }
    else{
        for(i = 2; i <= n; i++){
            answer += i ** 2;
            i += 1
        }
    }
    return answer;
}