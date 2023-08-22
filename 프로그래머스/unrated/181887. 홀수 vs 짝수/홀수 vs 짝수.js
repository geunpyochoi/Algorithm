function solution(num_list) {
    var answer = 0;
    let odd = 0;
    let even = 0;
    for(let i = 0; i < num_list.length; i++){
        if (i % 2 === 0) odd += num_list[i];
        else even += num_list[i];
    }
    return answer = odd > even ? odd : even;
}