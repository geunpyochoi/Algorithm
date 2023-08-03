function solution(k, m, score) {
    var answer = 0;
    score.sort((a,b)=>a-b);
    let l = score.length;
    for(let i = 0; i < l; i++){
        let box = [];
        let price = 0;
        if (score.length < m){
            break;
        }
        else{
            for(let j = 0; j < m; j++){
                box.push(score.pop());
            }
        }
        price = Math.min(...box) * box.length;
        answer += price;
    }
    return answer;
}