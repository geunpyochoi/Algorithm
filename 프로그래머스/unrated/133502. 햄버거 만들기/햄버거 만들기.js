function solution(ingredient) {
    var answer = 0;
    let stk = [];
    for(let i = 0; i <= ingredient.length; i++){
        if(ingredient[i] === 1 && stk.at(-1) === 3){
            stk.pop();
            stk.pop();
            stk.pop();
            answer += 1;
        }
        else if(ingredient[i] === 1) stk.push(ingredient[i]);
        
        else if(ingredient[i] === stk.at(-1)+1) stk.push(ingredient[i]);
        else{
            stk = [];
        }
        
    }
    return answer;
}