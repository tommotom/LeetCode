function lengthOfLastWord(s: string): number {
    let i = s.length - 1;
    while (s.charAt(i) === ' ') {
        i--;
    }
    let j = i;
    while (j >= 0 && s.charAt(j) !== ' ') {
        j--;
    }
    return i - j;
};
