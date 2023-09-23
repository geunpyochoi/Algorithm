function solution(arr) {
    var answer = 0;
    for(let i = 0; i < arr.length-1; i++){
        if (arr[i+1]%arr[i] === 0) continue;
        else{
            let n = 1;
            while(true){
                if (n%arr[i]===0 && n%arr[i+1]===0) {
                    arr[i+1] = n;
                    break;
                }
                else n++;
            }
        }
    }
    return arr[arr.length-1];
}