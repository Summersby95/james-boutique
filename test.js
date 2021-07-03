/* Create function that takes two arrays as arguments and returns 
new array with all elements */
function merge(arr1, arr2) {
  var newArr = [];
  for (var i = 0; i < arr1.length; i++) {
    newArr.push(arr1[i]);
  }
  for (var j = 0; j < arr2.length; j++) {
    newArr.push(arr2[j]);
  }
  return newArr;
}

/* Create function that takes two dates as arguments and returns 
difference between them in days */
function daysBetween(date1, date2) {
  var oneDay = 24 * 60 * 60 * 1000;
  var diff = Math.abs(date1.getTime() - date2.getTime());
  return Math.round(diff / oneDay);
}