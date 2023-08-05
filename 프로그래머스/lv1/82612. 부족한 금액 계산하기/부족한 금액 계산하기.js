function solution(price, money, count) {
    var answer = 0;
    for(let i = 1; i <= count; i++){
        answer += price * i;
    }
    if (answer-money < 0){
        answer = 0;
    }
    else{
        answer -= money;
    }
    return answer;
}