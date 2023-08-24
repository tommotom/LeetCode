function fullJustify(words: string[], maxWidth: number): string[] {
    const arr = [], ans = []
    let l = 0;
    for (const w of words) {
        arr.push(w);
        l += w.length;
        if (l + arr.length - 1 > maxWidth) {
            const tmp = arr.pop();
            l -= tmp.length;
            let space = (maxWidth - l);
            const a = [];
            while (arr.length > 0) {
                a.push(arr.shift());
                if (arr.length > 0) {
                    a.push(' '.repeat(Math.ceil(space/arr.length)));
                    space -= Math.ceil(space/arr.length);
                }
            }
            if (space > 0) {
                a.push(' '.repeat(space));
            }
            l = tmp.length;
            arr.push(tmp);
            ans.push(a.join(''));
        }
    }
    const str = arr.join(' ');
    ans.push(str + ' '.repeat(maxWidth-str.length));
    return ans;
};
