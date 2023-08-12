function solution(players, callings) {
    var answer = [];
    const idx = {};
    for(let i = 0 ; i < players.length; i++){
        idx[players[i]] = i;
    }
    for(let i = 0; i < callings.length; i++){
        let index = idx[callings[i]]; // 3
        let tmp = players[index - 1]; // poe
        
        players[index] = tmp;
        players[index-1] = callings[i];
            
        idx[tmp] = index;
        idx[callings[i]] = index-1;
        
        
    }
    return players;
}