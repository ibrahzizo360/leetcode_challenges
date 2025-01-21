/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const normalized = s.toLowerCase().split('')
    .filter(char => (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')).join('');

    const reversed = normalized.split('').reverse().join('');
    if (normalized == reversed){
        return true
    } else {
        return false
    }
};