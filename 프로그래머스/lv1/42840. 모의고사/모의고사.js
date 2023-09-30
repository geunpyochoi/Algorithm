function solution(answers) {
    var answer = [];
    let s1 = 0;
    let s2 = 0;
    let s3 = 0;
    for(let i = 1; i <= answers.length; i++){
        if (i % 5 === 0 && answers[i-1] === 5) s1 += 1;
        else if (i % 5 === answers[i-1]) s1 += 1;
    }
    for(let i = 0; i <= answers.length; i++){
        if (i % 2 === 0 && answers[i] === 2) s2 += 1;
        else if (i % 8 === 1 && answers[i] === 1) s2 += 1;
        else if (i % 8 === 3 && answers[i] === 3) s2 += 1;
        else if (i % 8 === 5 && answers[i] === 4) s2 += 1;
        else if (i % 8 === 7 && answers[i] === 5) s2 += 1;
    }
    for(let i = 0; i < answers.length; i++){
        if ((i % 10 === 0 || i % 10 === 1) && answers[i] === 3) s3 += 1;
        else if ((i % 10 === 2 || i % 10 === 3) && answers[i] === 1) s3 += 1;
        else if ((i % 10 === 4 || i % 10 === 5) && answers[i] === 2) s3 += 1;
        else if ((i % 10 === 6 || i % 10 === 7) && answers[i] === 4) s3 += 1;
        else if ((i % 10 === 8 || i % 10 === 9) && answers[i] === 5) s3 += 1;
    }
    if (s1 === s2 && s2 === s3){
        answer.push(1);
        answer.push(2);
        answer.push(3);
    }
    else if (s1 > s3 && s1 === s2){
        answer.push(1);
        answer.push(2);
    }
    else if (s1 > s2 && s1 === s3){
        answer.push(1);
        answer.push(3);
    }else if (s2 > s1 && s2 === s3){
        answer.push(2);
        answer.push(3);
    } else if (s1 > s2 && s1 > s3){
        answer.push(1);
    }
    else if (s2 > s1 && s2 > s3){
        answer.push(2);
    }
    else if (s3 > s2 && s3 > s1){
        answer.push(3);
    }
    return answer;
}