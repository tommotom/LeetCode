function takeCharacters(s: string, k: number): number {
    const isValid = counter => {
        return counter.get('a') >= k && counter.get('b') >= k && counter.get('c') >= k;
    }
    const counter = new Map();
    counter.set('a', 0);
    counter.set('b', 0);
    counter.set('c', 0);
    for (const c of s.split('')) {
        counter.set(c, counter.get(c) + 1);
    }

    if (!isValid(counter)) {
        return -1
    }

    let ans = s.length, l = s.length, r = s.length;
    while (l >= 0 && l <= r) {
        if (isValid(counter)) {
            ans = Math.min(ans, s.length - r + l);
            l--;
            counter.set(s.charAt(l), counter.get(s.charAt(l))-1);
        } else {
            r--;
            counter.set(s.charAt(r), counter.get(s.charAt(r))+1);
        }
    }
    return ans;
};
