function solution(number) {
    var answer = 0;
    number = number.split('');
    for(let i = 0; i < number.length; i++){
        answer += +number[i];
    }
    return answer%9;
}