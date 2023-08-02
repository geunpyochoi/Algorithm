function solution(n, arr1, arr2) {
    var answer = [];
    for (let i = 0; i < n; i++){
        let num = (arr1[i] | arr2[i]).toString(2);
        num = num.padStart(n,'0');
        answer.push(num.replaceAll('1','#').replaceAll('0',' '));
    }
    return answer;
}