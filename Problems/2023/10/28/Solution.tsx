const graph = new Map<string, string[]>([['a', ['e']], ['e', ['a', 'i']], ['i', ['a', 'e', 'u', 'o']], ['o', ['i', 'u']], ['u', ['a']]]);
const mod = 1000000007;
const memo = new Map<string, number>();
function countVowelPermutation(n: number): number {
    function helper(prev: string, n: number): number {
        if (n === 0) {
            return 1;
        }
        const key = prev + n.toString();
        if (!memo.has(key)) {
            memo.set(key, graph.get(prev).map(c => helper(c, n-1)).reduce((a, b) => (a + b) % mod));
        }
        return memo.get(key);
    }
    return (helper('a', n-1) + helper('e', n-1) + helper('i', n-1) + helper('o', n-1) + helper('u', n-1)) % mod;
};
