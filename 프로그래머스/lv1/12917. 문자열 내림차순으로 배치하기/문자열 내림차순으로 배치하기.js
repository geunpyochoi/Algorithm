function solution(s) {
    var answer = '';
    s = s.split('').sort().reverse();
    return s.join('');
}