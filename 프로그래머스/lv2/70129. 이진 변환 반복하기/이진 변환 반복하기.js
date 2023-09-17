function solution(s) {
    const answer = [0];
    let cnt = 0;
    let l = 0;
    while(s.length !== 1){
        if(s.includes('0')){
            for(let i = 0; i < s.length; i++){
                if (s[i] === '0') cnt += 1;
            }
            s = s.replaceAll('0','');
        }
        l = s.length;
        s = String(l.toString(2));
        answer[0] += 1;
    }
    answer.push(cnt);
    return answer;
}