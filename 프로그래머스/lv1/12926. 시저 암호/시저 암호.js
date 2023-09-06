function solution(s, n) {
    var answer = '';
    for(let i = 0; i < s.length; i++){
        if(s[i] == ' ') {
            answer += ' ';
            continue;}
        else if (65 <= s.charCodeAt(i) && s.charCodeAt(i) <= 90) {
            if(s.charCodeAt(i)+n > 90){
                answer += String.fromCharCode(s.charCodeAt(i)+n-26);
            }
            else{
                answer += String.fromCharCode(s.charCodeAt(i)+n);
            }
        }
        else if (97 <= s.charCodeAt(i) && s.charCodeAt(i) <= 122){
            if(s.charCodeAt(i)+n > 122){
                answer += String.fromCharCode(s.charCodeAt(i)+n-26);
            }
            else{
                answer += String.fromCharCode(s.charCodeAt(i)+n);
            }
        }
    }
    return answer;
}