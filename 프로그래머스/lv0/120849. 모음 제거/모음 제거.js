function solution(my_string) {
    var answer = '';
    let arr = ['a','e','i','o','u'];
    return my_string.split('').filter(v => !arr.includes(v)).join('');;
}