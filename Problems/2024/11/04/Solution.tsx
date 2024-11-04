function compressedString(word: string): string {
    let char = word.charAt(0), count = 0;
    const comp = [];
    for (const c of word) {
        if (char !== c || count === 9) {
            comp.push(count);
            comp.push(char);
            count = 0;
        }
        char = c;
        count++;
    }
    comp.push(count);
    comp.push(char);
    return comp.join('');
};
