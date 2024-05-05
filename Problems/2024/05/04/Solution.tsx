function numRescueBoats(people: number[], limit: number): number {
    people.sort((a, b) => a - b);
    let ans = 0, l = 0;
    for (let r = people.length-1; l <= r; r--) {
        if (people[l] + people[r] <= limit) {
            l++;
        }
        ans++;
    }
    return ans;
};
