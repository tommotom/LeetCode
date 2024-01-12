function halvesAreAlike(s: string): boolean {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
    let count = 0;
    const half = s.length / 2;
    for (let i = 0; i < half; i++) {
        if (vowels.has(s.charAt(i))) {
            count++;
        }
    }
    for (let i = half; i < s.length; i++) {
        if (vowels.has(s.charAt(i))) {
            count--;
        }
    }
    return count === 0;
};
