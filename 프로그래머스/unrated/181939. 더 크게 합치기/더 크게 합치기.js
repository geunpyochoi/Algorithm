function solution(a, b) {
    var answer = 0;
    var ab = String(a)+String(b);
    var ba = String(b)+String(a);
    if (ab>ba){
        answer = Number(ab);
    }
    else{
        answer = Number(ba);
    }
    return answer;
}