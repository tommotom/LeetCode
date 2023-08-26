function isInterleave(s1: string, s2: string, s3: string): boolean {
    if (s1.length + s2.length !== s3.length) {
        return false;
    }
    const tried = new Set();
    function helper(i: number, j: number) {
        if (i === s1.length && j === s2.length) {
            return true;
        }
        const key = i.toString() + " " + j.toString();
        if (tried.has(key)) {
            return false;
        }
        if (i < s1.length && s1.charAt(i) === s3.charAt(i+j) && helper(i+1, j)) {
            return true;
        }
        if (j < s2.length && s2.charAt(j) === s3.charAt(i+j) && helper(i, j+1)) {
            return true;
        }
        tried.add(key);
        return false;
    }

    return helper(0, 0);
};
