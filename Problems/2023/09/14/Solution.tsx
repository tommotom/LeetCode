function findItinerary(tickets: string[][]): string[] {
    const graph: Map<string, string[]> = new Map();
    for (const [a, b] of tickets) {
        if (!graph.has(a)) {
            graph.set(a, []);
        }
        graph.get(a).push(b);
    }
    const used: Map<string, boolean[]> = new Map();
    for (const key of graph.keys()) {
        graph.get(key).sort();
        used.set(key, [...Array(graph.get(key).length)].map(_ => false));
    }

    const ans = ["JFK"]
    function helper(cur) {
        if (ans.length === tickets.length + 1) {
            return true;
        }
        if (!graph.has(cur)) {
            return false;
        }
        for (let i = 0; i < graph.get(cur).length; i++) {
            if (used.get(cur)[i]) {
                continue;
            }
            const next = graph.get(cur)[i];
            used.get(cur)[i] = true;
            ans.push(next);
            if (helper(next)) {
                return true;
            }
            ans.pop();
            used.get(cur)[i] = false;
        }
        return false;
    }

    helper("JFK");

    return ans;
};
