function solution(n) {
    var answer = 0;
    let cnt = 0;
    n = n.toString(2);
    for(let i = 0; i < n.length; i++){
        cnt += n[i] === '1' ? 1 : 0;
    }
    let num = parseInt(n,2)+1;
    while(true){
        let cnt2 = 0;
        answer = num;
        num = num.toString(2);
        for(let i = 0; i < num.length; i++){
            cnt2 += num[i] === '1' ? 1 : 0;
        }
        if (cnt === cnt2) break;
        else num = parseInt(num,2) + 1;
    }
    return answer;
}