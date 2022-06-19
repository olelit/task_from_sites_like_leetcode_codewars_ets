/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let merge = sortArray(nums1, nums2);
  let len = merge.length;
  let center = Math.floor(len / 2);

  if (len % 2 !== 0) {
    return merge[center];
  }

  return (merge[center] + merge[center - 1]) / 2;
};

var sortArray = function (nums1, nums2) {
  let num1Index = 0;
  let num2Index = 0;
  let sorted = [];
  
  while (num1Index < nums1.length || num2Index < nums2.length) {
    let num1El = nums1[num1Index];
    let num2El = nums2[num2Index];
    if (num1El < num2El || (num2El === undefined && num1El !== undefined)) {
      sorted.push(num1El);
      num1Index++;
    }

    if (num1El >= num2El || (num1El === undefined && num2El !== undefined)) {
      sorted.push(num2El);
      num2Index++;
    }
  }

  return sorted;
};

let nums1 = [],
nums2 = [1, 2, 3, 4, 5];
console.log(findMedianSortedArrays(nums1, nums2));

(nums1 = [1, 3]), (nums2 = [2]);
console.log(findMedianSortedArrays(nums1, nums2));

(nums1 = [2]), (nums2 = []);
console.log(findMedianSortedArrays(nums1, nums2));

(nums1 = []), (nums2 = [1]);
console.log(findMedianSortedArrays(nums1, nums2));

(nums1 = [1, 2]), (nums2 = [3, 4]);
console.log(findMedianSortedArrays(nums1, nums2));
