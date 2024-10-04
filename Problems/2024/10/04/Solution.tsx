function dividePlayers(skill: number[]): number {
    skill = skill.sort((a, b) => a - b);
    const n = skill.length;
    const total = skill[0] + skill[n-1];
    let i = 0, ans = 0;
    while (i < n-i-1) {
        if (skill[i] + skill[n-i-1] !== total) {
            return -1;
        }
        ans += skill[i] * skill[n-i-1];
        i++;
    }
    return ans;
};
