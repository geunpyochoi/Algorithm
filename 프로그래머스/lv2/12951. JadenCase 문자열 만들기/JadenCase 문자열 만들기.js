function solution(s) {
    s = s.split(' ');
    
    s.forEach((v,i)=>{
        s[i] = v === '' ? '' : v[0].toUpperCase() + v.substr(1).toLowerCase();
    });
    return s.join(' ');
}