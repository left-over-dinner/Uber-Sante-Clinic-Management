import moment from 'moment';


export function CalculateAvailability(data) {
    let array = [];
    let index = 1;
    let pointerNumber = 0;
    var initialTime = moment("0800", "hhmm").format("HH:mm");
    var time = moment("0800", "hhmm").format("HH:mm");
    data.map(numbers=>{
        if(data[index] === numbers+1) {
            pointerNumber=numbers;
        }else{
            time = moment("0800", "hhmm").format("HH:mm");
            time = moment(time, 'HH:mm').add((numbers)*20, 'minutes').format('HH:mm');
            array.push(initialTime+'-'+time)
            initialTime = moment("0800", "hhmm").format("HH:mm");
            initialTime = moment(initialTime, 'HH:mm').add(numbers*20, 'minutes').format('HH:mm');
        }
        index = index + 1;

    });
    console.log(array)

}