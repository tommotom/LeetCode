function isPrefixOfWord(sentence: string, searchWord: string): number {
    const isPrefix = (word, pre) => {
        for (let i = 0; i < pre.length; i++) {
            if (word.length === i || word.charAt(i) !== pre.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    const arr = sentence.split(' ');
    for (let i = 0; i < arr.length; i++) {
        if (isPrefix(arr[i], searchWord)) {
            return i+1;
        }
    }
    return -1;
};
