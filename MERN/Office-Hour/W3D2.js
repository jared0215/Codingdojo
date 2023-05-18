var longestCommongPrefix = function (strs) {
    let prefix = "";
    if (strs.length === 0) return prefix;
    for (let i = 0; i < strs[0].length; i++) {
        for (let j = 1; j < strs.length; j++) {
            if (strs[j][i] !== strs[0][i]) return prefix;
        }
        prefix += strs[0][i];
    }
    return prefix;
};

console.log(longestCommongPrefix(["flower", "flow", "flight"]));
