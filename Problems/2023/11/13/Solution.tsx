function sortVowels(s: string): string {

    function isVowel(c: string): boolean {
        c = c.toLowerCase();
        return c === 'a' || c === 'i' || c === 'u' || c === 'e' || c === 'o';
    }

    const vowels = [];
    for (let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        if (isVowel(c)) {
            vowels.push(c);
        }
    }
    vowels.sort();

    const ret = [];
    for (let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        if (isVowel(c)) {
            ret.push(vowels.shift());
        } else {
            ret.push(c);
        }
    }

    return ret.join('');
};
