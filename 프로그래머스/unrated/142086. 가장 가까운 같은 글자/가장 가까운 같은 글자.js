function solution(s) {
    var answer = [];
    answer.push(-1);
    for(i=1; i < s.length; i++){
        for(j=i-1; j >= 0; j--){
            if (s[j] == s[i]){
                answer.push(i-j);
                break;
            }
        }
        if(answer.length != i+1){
            answer.push(-1);
        }
    }
    return answer;
}