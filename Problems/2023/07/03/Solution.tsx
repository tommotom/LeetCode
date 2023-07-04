function buddyStrings(s: string, goal: string): boolean {
    if (s.length !== goal.length) {
        return false;
    }

    const counter = (s: string): Map<string, number> => {
        const counter: Map<string, number> = new Map();
        for (let i = 0; i < s.length; i++) {
            if (!counter.has(s.charAt(i))) {
                counter.set(s.charAt(i), 0);
            }
            counter.set(s.charAt(i), counter.get(s.charAt(i))+1);
        }
        return counter;
    }

    const c1 = counter(s);
    const c2 = counter(goal);

    if (s === goal) {
        for (const count of c1.values()) {
            if (count > 1) {
                return true;
            }
        }
        return false;
    }

    for (const key of c1.keys()) {
        if (!c2.has(key) || c1.get(key) !== c2.get(key)) {
            return false;
        }
    }
    let diff = 0;
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) !== goal.charAt(i)) {
            diff++;
        }
    }
    return diff === 2;
};
