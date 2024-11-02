function isCircularSentence(sentence: string): boolean {
    const arr = sentence.split(' ');
    for (let i = 0; i < arr.length-1; i++) {
        const a = arr[i], b = arr[i+1];
        if (a.charAt(a.length-1) !== b.charAt(0)) {
            return false;
        }
    }
    return arr[0].charAt(0) === arr[arr.length-1].charAt(arr[arr.length-1].length-1);
};
