function minimumLength(s: string): number {
    let i = 0, j = s.length-1;
    while (i < j && s.charAt(i) === s.charAt(j)) {
        while (i+1 < j && s.charAt(i) === s.charAt(i+1)) {
            i++;
        }
        while (i < j-1 && s.charAt(j-1) === s.charAt(j)) {
            j--;
        }
        i++;
        j--;
    }
    return j - i + 1;
};
