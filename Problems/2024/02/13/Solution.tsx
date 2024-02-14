function firstPalindrome(words: string[]): string {
    function isPalin(word) {
        let i = 0, j = word.length - 1;
        while (i < j) {
            if (word.charAt(i++) !== word.charAt(j--)) {
                return false;
            }
        }
        return true;
    }

    for (const w of words) {
        if (isPalin(w)) {
            return w;
        }
    }
    return "";
};
