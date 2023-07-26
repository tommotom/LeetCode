function minSpeedOnTime(dist: number[], hour: number): number {

    function possible(v: number) {
        let took = 0;
        for (const d of dist) {
            if (took % 1 !== 0) {
                took = Math.ceil(took);
            }
            took += d / v;
        }
        return took <= hour;
    }

    let l = 1, r = 10000001;
    while (l < r) {
        const m = l + Math.floor((r-l)/2);
        if (possible(m)) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    console.log(l);
    return possible(l) ? l : -1;
};
