function arrayStringsAreEqual(word1: string[], word2: string[]): boolean {
    let i = 0, j = 0, ii = 0, jj = 0;
    while (i < word1.length && j < word2.length) {
        if (word1[i].charAt(ii) !== word2[j].charAt(jj)) {
            return false;
        }
        ii++;
        jj++;
        if (ii === word1[i].length) {
            ii = 0;
            i++;
        }
        if (jj === word2[j].length) {
            jj = 0;
            j++;
        }
    }
    return i == word1.length && j == word2.length;
};
