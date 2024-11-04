function rotateString(s: string, goal: string): boolean {
    if (s.length !== goal.length) {
        return false;
    }
    const n = s.length;
    for (let i = 0; i < n; i++) {
        let ok = true;
        for (let j = 0; j < n; j++) {
            if (s.charAt((i + j) % n) !== goal.charAt(j)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return true;
        }
    }
    return false;
};
