function reversePrefix(word: string, ch: string): string {
    let i = 0;
    while (i < word.length && word.charAt(i) !== ch) {
        i++;
    }
    return i < word.length ? word.substring(0, i+1).split('').reverse().join('') + word.substring(i+1) : word;
};
