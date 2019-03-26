import moment from 'moment';


export class TimeSlotConverter{


 convertArray(array){
  var sample =[
"08:00",
"08:20",
"08:40",
"09:00",
"09:20",
"09:40",
"10:00",
"10:20",
"10:40",
"11:00",
"11:20",
"11:40",
"12:00",
"12:20",
"12:40",
"13:00",
"13:20",
"13:40",
"14:00",
"14:20",
"14:40",
"15:00",
"15:20",
"15:40",
"16:00",
"16:20",
"16:40",
"17:00",
"17:20",
"17:40",
"18:00",
"18:20",
"18:40",
"19:00"
]

var result = [], temp = [], temp1 =[], difference;
for (var i = 0; i < array.length; i ++) {
    if (difference !== (array[i] - i)) {
        if (difference !== undefined) {
            result.push(temp);
            temp = [];
        }
        difference = array[i] - i;
    }
    temp.push(array[i]);
}

if (temp.length) {
    result.push(temp);
}


var final=[];
for (var i = 0; i < result.length; i ++)
{
  temp = sample[result[i][0]-1];
  var length= result[i].length-1;
  temp1 = sample[result[i][length]];
  var element = temp +"-"+ temp1;
  final.push(element);
}
return final;
}
}

