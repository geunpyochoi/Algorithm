function solution(a, b) {
    const day = ['THU','FRI','SAT','SUN','MON','TUE','WED'];
    let cnt = 0;
    for(let i = 1; i < a; i++){
        if (i === 2) cnt += 29;
        else if(i === 8) cnt += 31;
        else if((i < 8 && i % 2 === 1) || (i > 8 && i % 2 === 0)) cnt += 31;
        else if((i < 8 && i % 2 === 0) || (i > 8 && i % 2 === 1)) cnt += 30;
    }
    cnt += b;
    cnt = cnt % 7;
    return day[cnt];
}