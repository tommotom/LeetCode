impl Solution {
    pub fn read_binary_watch(turned_on: i32) -> Vec<String> {
        fn bit(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 2;
                num /= 2;
            }
            ret
        }

        fn hour(turned_on: i32) -> Vec<i32> {
            let mut ret = Vec::new();
            for h in 0..12 {
                if bit(h) == turned_on {
                    ret.push(h);
                }
            }
            ret
        }

        fn min(turned_on: i32) -> Vec<i32> {
            let mut ret = Vec::new();
            for m in 0..60 {
                if bit(m) == turned_on {
                    ret.push(m);
                }
            }
            ret
        }

        let mut ans = Vec::new();
        for i in 0..=turned_on {
            let hour = hour(turned_on - i);
            let min = min(i);
            for &h in &hour {
                for &m in &min {
                    ans.push(format!("{}:{:02}", h, m));
                }
            }
        }
        ans
    }
}
