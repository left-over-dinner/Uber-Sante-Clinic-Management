class TimeSlotConverter{


 convertArray(array){
  var sample =[
"8:00:00",
"8:20:00",
"8:40:00",
"9:00:00",
"9:20:00",
"9:40:00",
"10:00:00",
"10:20:00",
"10:40:00",
"11:00:00",
"11:20:00",
"11:40:00",
"12:00:00",
"12:20:00",
"12:40:00",
"13:00:00",
"13:20:00",
"13:40:00",
"14:00:00",
"14:20:00",
"14:40:00",
"15:00:00",
"15:20:00",
"15:40:00",
"16:00:00",
"16:20:00",
"16:40:00",
"17:00:00",
"17:20:00",
"17:40:00",
"18:00:00",
"18:20:00",
"18:40:00"
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

console.log(result);

var final=[];
for (var i = 0; i < result.length; i ++)
{
  temp = sample[result[i][0]-1];
  var length= result[i].length-1;
  temp1 = sample[result[i][length]];
  var element = temp +"-"+ temp1;
  console.log (element);
  final.push(element);
}
console.log(final);
return final;
}
}

//Run the method by doing like below
//i.e:
//var ben = [1,2,3,4,6,7,8,10];
//const myConverter = new TimeSlotConverter();
//myConverter.convertArray(ben);