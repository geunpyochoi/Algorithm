function solution(s){
    var answer = true;
    // const arr = [];
    // s = s.split('');
    // let i = -1;
    // while(s.length !== 0){
    //     arr.push(s.shift());
    //     if(arr.length >= 2 && (arr[i] === '(' && arr[i+1] === ')')){
    //         i--;
    //         arr.pop();
    //         arr.pop();
    //     } else i++;
    // }
    // return arr.length === 0 ? true : false;
    let n = 0;
    for(let i = 0; i < s.length; i++){
        if (n < 0){
            answer = false;
            break;
        }
        if (s[i] == '(') n += 1;
        else n -= 1;
        
        if(n > s.length) {
            answer = false;
            break;
        }
    }
    return answer = n === 0 ? true : false;
}