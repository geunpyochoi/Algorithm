function solution(progresses, speeds) {
    const answer = [];
    let i = 0;
    while(progresses.length !== 0){
        if(progresses[0] >= 100){
            progresses.shift();
            speeds.shift();
            if (answer.length < i+1) answer.push(0);
            answer[i]++;
            if(progresses[0] >= 100) continue;
            else i++;
            continue;
        }
        for(let j = 0; j < progresses.length; j++){
            progresses[j] += speeds[j];
        }
    }
    return answer;
}