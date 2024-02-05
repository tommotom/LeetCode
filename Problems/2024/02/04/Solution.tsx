function minWindow(s: string, t: string): string {

    function indexOf(c) {
        return c.charCodeAt(0) - "A".charCodeAt(0);
    }

    function isValid(counter, seenAt) {

        for (let i = 0; i < 58; i++) {
            if (counter[i] > seenAt[i].length) {
                return false;
            }
        }
        return true;
    }

    const counter = new Array(58).fill(0);
    for (const c of t) {
        counter[indexOf(c)] += 1
    }

    const seenAt = new Array(58).fill(0).map(()=>[]);
    let ans = "";
    for (let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        seenAt[indexOf(c)].push(i);
        if (seenAt[indexOf(c)].length > counter[indexOf(c)]) {
            seenAt[indexOf(c)].shift();
        }
        if (!isValid(counter, seenAt)) {
            continue;
        }
        let l = s.length, r = 0;
        for (let j = 0; j < 58; j++) {
            if (counter[j] > 0) {
                l = Math.min(l, seenAt[j][0]);
                r = Math.max(r, seenAt[j][seenAt[j].length-1]);
            }
        }
        if (ans === "" || ans.length > r - l + 1) {
            ans = s.substring(l, r+1);
        }
    }
    return ans;
};
