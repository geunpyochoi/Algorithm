function solution(food) {
    var answer = '';
    var s1 = '';
    var s2 = '';
    for(let i = 1; i < food.length; i++){
        if(food[i]%2 == 1){
            food[i] -= 1;
        }
        for (let j = 0; j < food[i]/2; j++){
            s1 += i;
        }
    }
    answer = s1 + '0';
    for(let k = s1.length-1; k >= 0; k--){
        answer += s1[k];
    }
    return answer;
}