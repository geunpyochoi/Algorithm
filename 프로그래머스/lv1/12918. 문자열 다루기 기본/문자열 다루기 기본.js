function solution(s) {
    var answer = true;
    s = s.split('');
    if (s.length === 4 || s.length === 6) {
        for(let i = 0; i < s.length; i++) {
        if(isNaN(s[i])){
            answer = false;
            break;
        }
    }
    }
    else return false;
    
    return answer;
}