function solution(k, score) {
    var answer = [];
    var arr = [];
    var idx = 0;
    for(i = 0; i < score.length; i++){
        if (i < k){
            arr.push(score[i]);
        }
        else{
            if (score[i] > Math.min(...arr)){
                idx = arr.indexOf(Math.min(...arr));
                arr[idx] = score[i];
            }
        }
        answer.push(Math.min(...arr));
    }
    return answer;
}