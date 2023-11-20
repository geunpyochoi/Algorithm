function solution(dart) {
    dart = dart.split('');
    let n = [0,0,0]
    let p = 0;
    for(let i = 0; i < dart.length; i++){
        if (!isNaN(dart[i])){
            if (!isNaN(dart[i-1])){
                n[p] = 10;
            }
            else{
                n[p] = +dart[i];
            }
        }
        else if(dart[i] === 'S'||dart[i] === 'D'||dart[i] === 'T'){
            if(dart[i] === 'D'){
                n[p] = n[p]**2;
            }
            else if (dart[i] === 'T') n[p] = n[p]**3;
            if (dart[i+1] !== '*' && dart[i+1] !== '#'){
                p++;
            }
        }
        else{
            if (dart[i] === '*'){
                n[p] *= 2;
                n[p-1] *= 2;
            }
            else{
                n[p] *= -1;
            }
            p++;
        }
    }
    
    return n.reduce((a,c)=>a+c,0);
}