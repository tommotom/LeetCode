function poorPigs(buckets: number, minutesToDie: number, minutesToTest: number): number {
    return Math.ceil(Math.log2(buckets) / Math.log2(Math.floor(minutesToTest / minutesToDie) + 1));
};
