function countRoutes(locations: number[], start: number, finish: number, fuel: number): number {

    const mod = 1000000007;
    const dp = new Array(locations.length);
    for (let i = 0; i < locations.length; i++) {
        dp[i] = new Array(fuel);
    }

    const helper = (i, target) => {
        if (target > fuel) {return 0;}
        if (dp[i][target] !== undefined) {
            return dp[i][target];
        }
        let ret = i === start ? 1 : 0;
        for (let j = 0; j < locations.length; j++) {
            if (i === j) {continue;}
            ret += helper(j, target + Math.abs(locations[i] - locations[j]));
            ret %= mod
        }
        dp[i][target] = ret;
        return ret;
    }

    return helper(finish, 0);
};
