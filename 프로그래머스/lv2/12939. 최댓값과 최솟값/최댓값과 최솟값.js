function solution(s) {
    var answer = '';
    s = s.split(' ');
    s.forEach((v,i)=>{
        s[i] = parseInt(v);
    })
    answer += Math.min(...s);
    answer += ' ';
    answer += Math.max(...s);
    return answer;
}