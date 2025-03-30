impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let m = 1 + nums.iter().max().unwrap().clone() as usize;
        let mut prime_scores = vec![0; m];

        for x in 2..m {
            if prime_scores[x] == 0 {
                for v in (x..m).step_by(x) {
                    prime_scores[v] += 1
                }
            }
        }

        let mut left_count = vec![0_usize; n];
        let mut left_border = Vec::<usize>::new();

        for l in 0..n {
            while !left_border.is_empty() {
                if prime_scores[nums[left_border.last().unwrap().clone()] as usize] >= prime_scores[nums[l] as usize] {
                    break;
                }

                left_border.pop();
            }

            if left_border.is_empty() {
                left_count[l] += l
            } else {
                left_count[l] += l - left_border.last().unwrap().clone() - 1
            }

            left_border.push(l);
        }

        let mut right_count = vec![0_usize; n];
        let mut right_border = Vec::<usize>::new();

        for r in (0..n).rev() {
            while !right_border.is_empty() {
                if prime_scores[nums[r] as usize] < prime_scores[nums[right_border.last().unwrap().clone()] as usize] {
                    break;
                }

                right_border.pop();
            }

            if right_border.is_empty() {
                right_count[r] += n - r - 1
            } else {
                right_count[r] += right_border.last().unwrap().clone() - r - 1
            }

            right_border.push(r);
        }

        let mut ii = (0..n).collect::<Vec<usize>>();

        ii.sort_unstable_by_key(|i| std::cmp::Reverse(nums[*i]));

        let mut remain = k as usize;
        let mut result = 1 as usize;

        const MOD: usize = (1e9 as usize) + 7;

        for i in ii {
            if remain == 0 {
                break;
            }

            let mut x = nums[i] as usize;
            let mut c = remain.min((left_count[i] + 1) * (right_count[i] + 1));

            remain -= c;

            while c > 0 {
                if c % 2 == 1 {
                    result *= x;
                    result %= MOD;
                }

                x *= x;
                x %= MOD;

                c /= 2;
            }
        }

        result as i32
    }
}
