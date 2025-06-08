impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        fn to_num(arr: &Vec<i32>) -> i32 {
            let mut ret = 0;
            for num in arr {
                ret *= 10;
                ret += *num;
            }
            ret
        }

        fn dfs(arr: &mut Vec<i32>, ans: &mut Vec<i32>, n: i32) {
            for d in 0..10 {
                if d == 0 && arr.len() == 0 {
                    continue;
                }
                arr.push(d);
                let num = to_num(arr);
                if num <= n {
                    ans.push(num);
                    dfs(arr, ans, n);
                }
                arr.pop();
                if num > n {
                    break;
                }
            }
        }

        let mut ans = Vec::new();
        let mut arr = Vec::new();

        dfs(&mut arr, &mut ans, n);

        ans
    }
}
