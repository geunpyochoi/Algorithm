const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    l = str.length;
    answer = '';
    for(i = 0; i < l; i++){
        if(str[i].toUpperCase() == str[i]){
            answer += str[i].toLowerCase();
        }
        else{
            answer += str[i].toUpperCase();
        }
    }
    console.log(answer);
});