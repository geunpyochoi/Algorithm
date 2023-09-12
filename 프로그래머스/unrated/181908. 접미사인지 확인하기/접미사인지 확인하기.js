function solution(my_string, is_suffix) {
    var answer = 0;
    return answer = my_string.slice(my_string.length-is_suffix.length) === is_suffix ? 1 : 0;
}