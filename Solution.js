// Factoryas Calculation In Javascript



a =[1,2,23,24,2,3,1,3]

console.log(a)
for(let i=0;i<a.length;i++) {
    for(let j=i+1;j<a.length;j++) {
        if(a[i] > a[j]) {
            let temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }
}
console.log(a)