function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    const isCollide = (arr, robo) => {
        return arr.length > 0 && arr[arr.length-1][2] === 'R' && robo[2] === 'L';
    }

    const robots = [];
    for (let i = 0; i < positions.length; i++) {
        robots.push([positions[i], healths[i], directions[i], i]);
    }
    robots.sort((a, b) => a[0] - b[0]);

    const st = [];
    let i = 0;
    for (let i = 0; i < robots.length; i++) {
        while (isCollide(st, robots[i]) && st[st.length-1][1] < robots[i][1] && robots[i][1] > 0) {
            st.pop();
            robots[i][1] -= 1;
        }
        if (robots[i][1] === 0) {
            continue;
        }
        if (isCollide(st, robots[i])) {
            if (st[st.length-1][1] === robots[i][1]) {
                st.pop();
            } else {
                st[st.length-1][1] -= 1
                if (st[st.length-1][1] === 0) {
                    st.pop();
                }
            }
        } else {
            st.push(robots[i]);
        }
    }

    st.sort((a, b) => a[3] - b[3]);

    return st.map(a => a[1]);
};
