/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

//leetcode живет немного в другом веке =)

var twoSum = function (nums, target) {
  for (let first = 0; first < nums.length; first++) {
    let firstMapEl = nums[first];
    for (let second = 0; second < nums.length; second++) {
      let secondMapEl = nums[second];
      if (first !== second) {
        if (firstMapEl + secondMapEl === target) {
          return [first, second];
        }
      }
    }
  }
  return [];
};

//короче и читается лучше, но leetcode считает что это работает медленнее
const twoSum2 = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    let second = target - nums[i];
    let secondIndex = nums.indexOf(second);
    if (secondIndex !== -1 && secondIndex !== i) {
      return [i, secondIndex];
    }
  }

  return [];
};

const nums = [3, 3];
const target = 6;

console.log(twoSum(nums, target));
