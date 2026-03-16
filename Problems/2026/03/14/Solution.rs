impl Solution {
    pub fn get_happy_string(n: i32, mut k: i32) -> String {

        let total = 3 * (1 << (n-1));
        if k > total { return "".to_string(); }

        k -= 1;

        let mut res = String::new();
        let mut last = '\0';

        for pos in 0..n {

            let branch = 1 << (n-pos-1);

            let mut choices = vec![];
            for c in ['a','b','c'] {
                if c != last { choices.push(c); }
            }

            let idx = (k / branch) as usize;

            res.push(choices[idx]);
            last = choices[idx];

            k %= branch;
        }

        res
    }
}
