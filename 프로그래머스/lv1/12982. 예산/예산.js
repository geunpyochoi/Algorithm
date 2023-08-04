function solution(d, budget) {
    var answer = 0;
    d.sort((a,b)=>b-a);
    while(budget >= d[d.length-1]){
        budget -= d.pop();
        answer += 1;
    }
    return answer;
}