impl Solution {
    pub fn get_happy_string(n: i32, mut k: i32) -> String {
        if k > 3 * 2_i32.pow(n as u32 - 1) {
            return "".to_string();
        }
        let mut rest = 2_i32.pow(n as u32 - 1);
        let mut ans = Vec::new();
        if k <= rest {
            ans.push('a');
        } else if k <= 2 * rest {
            ans.push('b');
            k -= rest;
        } else {
            ans.push('c');
            k -= rest * 2;
        }
        rest /= 2;

        for i in 1..(n as usize) {
            if k <= rest {
                ans.push(if ans[i-1] == 'a' {'b'} else {'a'});
            } else {
                ans.push(if ans[i-1] == 'c' {'b'} else {'c'});
                k -= rest;
            }
            rest /= 2;
        }
        ans.iter().collect()
    }
}
