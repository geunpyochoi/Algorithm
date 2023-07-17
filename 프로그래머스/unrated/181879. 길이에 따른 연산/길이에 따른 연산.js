function solution(num_list) {
    var answer = 0;
    len = num_list.length;
    if (len >= 11){
        for(i = 0; i < len; i++){
            answer += num_list[i];
        }
    }
    else{
        answer = 1;
        for(i = 0; i < len; i++){
            answer *= num_list[i];
        }
    }
    return answer;
}