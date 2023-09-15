function solution(myString) {
    var answer = '';
    myString = myString.toLowerCase();
    myString = myString.split('');
    for(let i = 0; i < myString.length; i++){
        if (myString[i] === 'a'){
            myString[i] = myString[i].toUpperCase();
        }
    }
    return myString.join('');
}