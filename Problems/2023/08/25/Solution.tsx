function isInterleave(s1: string, s2: string, s3: string): boolean {
    if (s1.length + s2.length !== s3.length) {
        return false;
    }
    const memo = new Map();
    function helper(s1: string, s2: string, s3: string): boolean {
        if (s1.length === 0) {
            return s2 === s3;
        }
        if (s2.length === 0) {
            return s1 === s3;
        }

        const key = s1 + " " + s2;

        if (memo.has(key)) {
            return memo.get(key);
        }

        if (s1.substring(0, 1) == s3.substring(0, 1) && isInterleave(s1.substring(1), s2, s3.substring(1))) {
            memo.set(key, true);
            return true;
        }

        if (s2.substring(0, 1) == s3.substring(0, 1) && isInterleave(s1, s2.substring(1), s3.substring(1))) {
            memo.set(key, true);
            return true;
        }
        return false;
    }

    return helper(s1, s2, s3);
};
