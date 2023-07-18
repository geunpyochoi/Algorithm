function solution(my_string, overwrite_string, s) {
    var answer = '';
    var my = [...my_string];
    my.splice(s,overwrite_string.length,overwrite_string); // s부터 overwrite만큼 삭제하고 overwrite를 쓴다.
    answer = my.join('');
    return answer;
}