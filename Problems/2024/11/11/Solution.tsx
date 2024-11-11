function primeSubOperation(nums: number[]): boolean {
    const isPrime = Array(1001).fill(true);
    const primes = [];
    isPrime[1] = false;
    for (let num = 2; num < 1001; num++) {
        if (!isPrime[num]) {
            continue;
        }
        primes.push(num);
        let x = 2;
        while (num * x < 1001) {
            isPrime[num * x] = false;
            x++;
        }
    }

    primes.reverse();

    for (let i = 0; i < nums.length; i++) {
        for (const p of primes) {
            if (nums[i] > p && (i === 0 || nums[i] - p > nums[i-1])) {
                nums[i] -= p;
                break;
            }
        }
    }

    for (let i = 1; i < nums.length; i++) {
        if (nums[i-1] >= nums[i]) {
            return false;
        }
    }

    return true;
};
