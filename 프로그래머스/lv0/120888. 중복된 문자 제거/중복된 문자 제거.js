function solution(my_string) {
    var answer = '';
    answer = my_string.split('');
    const set = new Set(answer);
    answer = [...set];
    return answer.join('');
}