function solution(left, right) {
    var answer = 0;
    let cnt = 0;
    for(let i = left; i <= right; i++){
        cnt = 0;
        for(let j = 1; j <= i; j++){
            if (i % j === 0) cnt++;
        }
        answer += cnt % 2 === 0 ? i : -i;
    }
    return answer;
}