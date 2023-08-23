function solution(arr) {
    var answer = [];
    let n = Math.min(...arr);
    arr.splice(arr.indexOf(n),1);
    return arr.length === 0 ? [-1] : arr;
}