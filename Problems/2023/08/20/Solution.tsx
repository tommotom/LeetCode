function sortItems(n: number, m: number, group: number[], beforeItems: number[][]): number[] {
    const itemSet: Map<number, Set<number>> = new Map();
    itemSet.set(-1, new Set());
    for (let i = 0; i < n; i++) {
        if (!itemSet.has(group[i])) {
            itemSet.set(group[i], new Set());
        }
        itemSet.get(group[i]).add(i);
    }

    const grpDep: Map<number, Set<number>> = new Map();
    const grpGraph: Map<number, Set<number>> = new Map();
    const nodeDep: Map<number, Set<number>> = new Map();
    const nodeGraph: Map<number, Set<number>> = new Map();
    for (let i = 0; i < n; i++) {
        for (const b of beforeItems[i]) {
            if (group[i] >= 0 && !itemSet.get(group[i]).has(b)) {
                if (!grpDep.has(group[i])) {
                    grpDep.set(group[i], new Set());
                }
                grpDep.get(group[i]).add(b);
                if (!grpGraph.has(b)) {
                    grpGraph.set(b, new Set());
                }
                grpGraph.get(b).add(group[i])
            } else {
                if (!nodeDep.has(i)) {
                    nodeDep.set(i, new Set());
                }
                nodeDep.get(i).add(b);
                if (!nodeGraph.has(b)) {
                    nodeGraph.set(b, new Set());
                }
                nodeGraph.get(b).add(i);
            }
            if (group[i] === -1) {

            }
        }
    }

    const ans: number[] = [];
    let last = 0;

    function proceed(g: number): void {
        while (true) {
            const q = [];
            for (const i of itemSet.get(g)) {
                if (!nodeDep.has(i) || nodeDep.get(i).size === 0) {
                    q.push(i);
                }
            }
            if (q.length === 0) {
                break;
            }
            for (const i of q) {
                ans.push(i);
                if (nodeGraph.has(i)) {
                    for (const next of nodeGraph.get(i)) {
                        nodeDep.get(next).delete(i);
                    }
                }
                if (grpGraph.has(i)) {
                    for (const next of grpGraph.get(i)) {
                        grpDep.get(next).delete(i);
                    }
                }
                itemSet.get(g).delete(i);
            }
        }
    }

    while (ans.length < n) {
        proceed(-1);
        for (const g of itemSet.keys()) {
            if (grpDep.has(g) && grpDep.get(g).size > 0) {
                continue;
            }
            proceed(g);
        }
        if (ans.length === last) {
            return [];
        }
        last = ans.length;
    }

    return ans;
};
