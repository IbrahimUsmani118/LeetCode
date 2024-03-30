/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */

var chunk = function(arr, size = arr.length) {
    // initialize variable result
    var result = [];
    // set your for loop i compared to arr.length and initialize i to add on from size.
    for (let i=0; i<arr.length; i+=size) {
            // pushes arr to slice based on index i and i+size based on size per testcase #
            result.push(arr.slice(i, i+size))
    }
    // returns updated result
    return result;
};
