function nextGreatestLetter(letters: string[], target: string): string {
    let l = 0;
    let r = letters.length;
    while (l < r) {
        let m = Math.floor(l + (r - l) / 2);
        if (letters[m] <= target) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l == letters.length ? letters[0] : letters[l];
}
