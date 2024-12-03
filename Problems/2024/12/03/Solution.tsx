function addSpaces(s: string, spaces: number[]): string {
    let i = 0;
    const ans = [];
    for (let j = 0; j < s.length; j++) {
        if (i < spaces.length && spaces[i] === j) {
            ans.push(' ');
            i++;
        }
        ans.push(s.charAt(j));
    }
    return ans.join('');
};
