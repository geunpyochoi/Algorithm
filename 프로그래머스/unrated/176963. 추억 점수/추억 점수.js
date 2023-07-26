function solution(name, yearning, photo) {
    var answer = [];
    var ans = 0;
    for(i = 0; i < photo.length; i++){
        for(j = 0; j < photo[i].length; j++){
            for(k = 0; k < name.length; k++){
                if (name[k] == photo[i][j]){
                    ans += yearning[k];
                }
            }
        }
        answer.push(ans);
        ans = 0;
    }
    return answer;
}