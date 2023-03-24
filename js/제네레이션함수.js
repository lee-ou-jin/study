function* range(start,end,step) {
    let current = start;
    while(current<=end){
        yield current;
        current += step || 1;
    }
}

const generator = range(1, 10 ,2);
let result = generator.next();

while(!result.done){
    console.log(result.value);
    result = generator.next();
}