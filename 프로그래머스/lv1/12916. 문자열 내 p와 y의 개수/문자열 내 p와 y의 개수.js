function solution(s){
    var answer = true;
    s = s.toLowerCase();
    let p = 0;
    let y = 0;
    for (let i = 0; i < s.length; i++){
        if (s[i] === 'p'){
            p += 1;
        }
        else if(s[i] === 'y'){
            y += 1;
        }
    }
    return answer = p === y ? true : false;;
}