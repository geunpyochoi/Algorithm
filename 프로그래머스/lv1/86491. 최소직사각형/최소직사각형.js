function solution(sizes) {
    var answer = 0;
    let tmp = 0;
    for(let i = 0; i < sizes.length; i++){
        if (sizes[i][1] > sizes[i][0]){
            tmp = sizes[i][1];
            sizes[i][1] = sizes[i][0];
            sizes[i][0] = tmp;
        }
    }
    let max1 = 0;
    let max2 = 0;
    for(let i = 0; i < sizes.length; i++){
        if(sizes[i][0] > max1) max1 = sizes[i][0];
    }
    for(let i = 0; i < sizes.length; i++){
        if(sizes[i][1] > max2) max2 = sizes[i][1];
    }
    return max1*max2;
}