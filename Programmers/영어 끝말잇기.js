function solution(n, words) {
    var answer = [0,0];
    let flag = 0;
    for(let i = 0; i < words.length-1; i++){
        for(let j = i+1; j < words.length; j++){
            if(words[i] === words[j]){
                answer[0] = (j%n)+1;
                answer[1] = parseInt(j/n)+1;
                flag = 1;
                break;
            }
        }
        if (flag === 1){
            break;
        }
        if (words[i].at(-1) !== words[i+1].at(0)){
            answer[0] = ((i+1)%n)+1;
            answer[1] = parseInt((i+1)/n)+1;
            break;
        }
    }

    return answer;
}
