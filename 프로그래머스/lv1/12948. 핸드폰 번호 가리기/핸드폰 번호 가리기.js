function solution(phone_number) {
    let l = phone_number.length-4;
    let answer = '';
    for(let i = 0; i < l; i++) answer += '*';
    answer += phone_number.slice(-4);
    return answer;
}