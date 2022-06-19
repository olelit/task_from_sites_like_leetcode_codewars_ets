/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    let elementInStorage = [];
    let max = 0;

    for(let index = 0; index < s.length; index++){
        let element = s[index] ?? ' ';
        let elemIndex = elementInStorage.indexOf(element);

        if(elemIndex != -1){
            max = Math.max(max, elementInStorage.length);
            elementInStorage = elementInStorage.slice(elemIndex+1); 
            elementInStorage.push(element);
        }
        else{
            elementInStorage.push(element);
        }
    }
    return Math.max(max, elementInStorage.length);
};

console.log(lengthOfLongestSubstring('abcabcbb'));
console.log(lengthOfLongestSubstring('bbbbb'));
console.log(lengthOfLongestSubstring('pwwkew'));
console.log(lengthOfLongestSubstring(' '));
console.log(lengthOfLongestSubstring('c'));
console.log(lengthOfLongestSubstring('dvdf'));