function solution(array, commands) {
    var answer = [];
    var arr = [];
    for (i = 0; i < commands.length; i++){
        arr = array.slice(commands[i][0]-1,commands[i][1]);
        arr.sort((a,b)=>a-b);
        answer.push(arr[commands[i][2]-1]);
        arr = [];

    }
    return answer;
}