function hoursMinutes(minutes){
    let hours = Math.floor(minutes/60)
    let mins = minutes % 60
    return `${hours} hours and ${mins} minutes`
}







console.log(hoursMinutes(125)) // => '2 hours and 5 minutes'
console.log(hoursMinutes(75)) // => '1 hour and 15 minutes'
console.log(hoursMinutes(55)) // => '0 hours and 55 minutes'
console.log(hoursMinutes(121)) // => '2 hours and 1 minute'