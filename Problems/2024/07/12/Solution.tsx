function maximumGain(s: string, x: number, y: number): number {
    let ans = 0;

    const removeAb = (arr) => {
        if (arr[arr.length-1] === 'b' && arr[arr.length-2] === 'a') {
            arr.pop();
            arr.pop();
            ans += x;
        }
    }

    const removeBa = (arr) => {
        if (arr[arr.length-1] === 'a' && arr[arr.length-2] === 'b') {
            arr.pop();
            arr.pop();
            ans += y;
        }
    }

    const st = [];
    for (const c of s) {
        st.push(c);
        if (st.length < 2) {
            continue;
        }
        if (x > y) {
            removeAb(st);
        } else {
            removeBa(st);
        }
    }

    const st2 = [];
    for (const c of st) {
        st2.push(c);
        if (st2.length < 2) {
            continue;
        }
        if (x > y) {
            removeBa(st2);
        } else {
            removeAb(st2);
        }
    }

    return ans;
};
