/**
 * @param {number[]} height
 * @return {number}
 */
// var maxArea = function (height) {
//   let max = 0;
//   for (let firstMap = 0; firstMap < height.length; firstMap++) {
//     let firstEl = height[firstMap];
//     for (let secondMap = firstMap+1; secondMap < height.length; secondMap++) {
//       let secondEl = height[secondMap];
//       let xLen = Math.abs(secondMap - firstMap);
//       let minHeight = Math.min(firstEl, secondEl);
//       let square = xLen * minHeight;
//       if (square > max){
//           max = square;
//       }
//     }
//   }

//   return max;
// };

var maxArea = function (height) {
  let start = 0;
  let length = height.length;
  let end = length - 1;
  let max = 0;
  while (start <= end) {
    let square = (end - start) * Math.min(height[start], height[end]);
    max = square > max ? square : max;
    if (height[start] > height[end]) {
      end--;
    } else {
      start++;
    }
  }

  return max;
};

let input = [1, 8, 6, 2, 5, 4, 8, 3, 7];
console.log(maxArea(input));
