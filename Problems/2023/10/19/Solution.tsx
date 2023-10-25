function backspaceCompare(s: string, t: string): boolean {
    function del(s: string, i: number): number {
        let del = 0;
        while (i >= 0) {
            if (s.charAt(i) === '#') {
                i--;
                del++;
            } else if (del > 0) {
                i--;
                del--;
            } else {
                break;
            }
        }
        return i;
    }

    let i = s.length-1, j = t.length-1;
    while (i >= 0 && j >= 0) {
        i = del(s, i);
        j = del(t, j);
        if (i >= 0 !== j >= 0) {
            return false;
        }
        if (i >= 0 && j >= 0 && s.charAt(i) !== t.charAt(j)) {
            return false;
        }
        i--;
        j--;
    }
    if (i >= 0) {
        i = del(s, i);
    }
    if (j >= 0) {
        j = del(t, j);
    }
    return i === j;
};
