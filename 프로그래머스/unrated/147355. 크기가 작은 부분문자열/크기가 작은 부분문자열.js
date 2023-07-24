function solution(t, p) {
    var answer = 0;
    var n = 0;
    var m = 0;
    for(i = 0; i < t.length-p.length+1; i++){
        if (t[i] <= p[0]){
            for(j = 0; j < p.length; j++){
                n += t[i+j];
                m += p[j];
            }
            if (Number(n) <= Number(m)){
                answer += 1;
            }
            n = 0;
            m = 0;
        }
    }
    return answer;
}