function solution(str1, str2) {
    var answer = '';
    l = str1.length;
    for(i = 0; i < l; i++){
        answer += str1[i] + str2[i];
    }
    return answer;
}