function countConsistentStrings(allowed: string, words: string[]): number {
    const allowedSet = new Set(allowed.split(''));
    return words.filter(word => word.split('').reduce((acc, cur) => acc && allowedSet.has(cur), true)).length;
    ;
};
