function divisible3y5(num){
    return (num%3===0) || (num%10===0) || (num%10===5)
}

console.log(divisible3y5(61)); // False
console.log(divisible3y5(120)); //True
