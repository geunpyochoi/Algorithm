function solution(brown, yellow) {
    var answer = [];
    const num = brown + yellow;
    let j = 0;
    for(let i = 3; i < num; i++){
        if (num%i===0) {
            j = num / i;
            if (((i-2)*2) + (j*2) === brown){
                answer.push(j,i);
                break;
            }
        } else {
            continue;
        }
    }
    return answer;
}
// 1 2 3 4 6 12   1 3 9
// 1 2 3 4 6 8 12 16 24 48
11111111
10000001
10000001
10000001
10000001
11111111