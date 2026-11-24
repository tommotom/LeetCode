impl Solution {
    pub fn max_length(nums: Vec<i32>) -> i32 {
        fn gcd(a: i32, b: i32) -> i32 {
            if b > a {
                return gcd(b, a);
            }
            if b == 0 {
                return a;
            }
            gcd(b, a % b)
        }
        fn prime(mut num: i32) -> Vec<i32> {
            let mut ret = vec![0; 10];
            while num % 2 == 0 {
                num /= 2;
                ret[2] += 1;
            }
            for d in (3..8).step_by(2) {
                while num % (d as i32) == 0 {
                    num /= (d as i32);
                    ret[d] += 1;
                }
            }
            ret
        }
        fn lcm(a: i32, b: i32) -> i32 {
            let a_p = prime(a);
            let b_p = prime(b);
            let mut ret = 1;
            for num in 2..10 {
                if a_p[num] > 0 || b_p[num] > 0 {
                    ret *= (num as i32).pow(a_p[num].max(b_p[num]) as u32)
                }
            }
            ret
        }
        let mut ans = 0;
        for l in 0..nums.len() {
            for r in (l+2)..=nums.len() {
                let mut prod = 1;
                for i in l..r {
                    prod *= nums[i];
                }
                let mut g = nums[l];
                let mut m = nums[l];
                for i in (l+1)..r {
                    g = gcd(g, nums[i]);
                    m = lcm(m, nums[i]);
                }
                if prod == g * m {
                    ans = ans.max((r - l) as i32)
                }
            }
        }

        ans
    }
}
