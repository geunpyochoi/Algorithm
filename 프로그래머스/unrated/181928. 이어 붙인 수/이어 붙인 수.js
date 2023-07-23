function solution(num_list) {
    var answer = 0;
    var odd = '';
    var even = '';
    for(i = 0; i < num_list.length; i++){
        if (num_list[i] %2 == 1){
            odd += String(num_list[i]);
        }
        else{
            even += String(num_list[i]);
        }
    }
    return Number(odd)+Number(even);
}