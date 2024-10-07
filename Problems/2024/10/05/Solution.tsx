function checkInclusion(s1: string, s2: string): boolean {
    const base = 'a'.charCodeAt(0);
    const count1 = Array(26).fill(0);
    for (const c of s1.split('')) {
        count1[c.charCodeAt(0) - base]++;
    }

    const count2 = Array(s2.length+1).fill(0).map(_ => Array(26).fill(0));
    for (let i = 1; i <= s2.length; i++) {
        for (let j = 0; j < 26; j++) {
            count2[i][j] = count2[i-1][j];
        }
        count2[i][s2.charCodeAt(i-1) - base]++;
        if (i >= s1.length) {
            let isValid = true;
            for (let j = 0; j < 26; j++) {
                if (count1[j] !== (count2[i][j] - count2[i-s1.length][j])) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                return true;
            }
        }
    }

    return false;
};
