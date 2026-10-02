impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        fn helper(n: i32, open: i32, close: i32, vec: &mut Vec<char>, res: &mut Vec<String>) {
            if n == open && n == close {
                res.push(vec.iter().collect());
                return;
            }
            if n > open {
                vec.push('(');
                helper(n, open + 1, close, vec, res);
                vec.pop();
            }
            if open > close {
                vec.push(')');
                helper(n, open, close + 1, vec, res);
                vec.pop();
            }
        }
        let mut vec = Vec::new();
        let mut res = Vec::new();
        helper(n, 0, 0, &mut vec, &mut res);
        res
    }
}
