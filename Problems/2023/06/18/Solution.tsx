const mod = 1000000007;
const dirs = [[0,1],[0,-1],[1,0],[-1,0]];

let m: number;
let n: number;
let dp: number[][];

function countPaths(grid: number[][]): number {
    m = grid.length, n = grid[0].length;
    dp = new Array(m);
    for (let i = 0; i < m; i++) { dp[i] = new Array(n); }
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            ans += helper(i, j, grid);
            ans %= mod;
        }
    }
    return ans;
};

function helper(i: number, j: number, grid: number[][]): number {
    if (dp[i][j] !== undefined) {
        return dp[i][j];
    }
    let ret = 1;
    for (const dir of dirs) {
        const I = i + dir[0], J = j + dir[1];
        if (I < 0 || I == m || J < 0 || J == n || grid[i][j] >= grid[I][J]) {
            continue;
        }
        ret += helper(I, J, grid);
        ret %= mod;
    }
    dp[i][j] = ret;
    return ret;
}
