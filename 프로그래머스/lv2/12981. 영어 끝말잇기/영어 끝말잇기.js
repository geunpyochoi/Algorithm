function solution(n, words) {
    var answer = [0,0];
    let flag = 0;
    for(let i = 1; i < words.length; i++){
        
        //중복체크
        for(let j = i-1; j >= 0; j--){
            if(words[i] === words[j]){
                answer[0] = (i%n)+1;
                answer[1] = parseInt(i/n)+1;
                flag = 1;
                break;
            }
        }
        if (flag === 1){
            break;
        }
        //끝말잇기 체크          
        if (words[i-1].at(-1) !== words[i].at(0)){
            answer[0] = ((i)%n)+1;
            answer[1] = parseInt((i)/n)+1;
            break;
        }
        
        
        
    }
    return answer;
}