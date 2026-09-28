impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let mut stack: Vec<String> = Vec::new();
        let mut current = String::new();

        for ch in s.chars() {

            if ch == '(' {
                stack.push(current);
                current = String::new();

            } else if ch == ')' {
                current = current.chars().rev().collect();

                let previous = stack.pop().unwrap();
                current = previous + &current;

            } else {
                current.push(ch);
            }
        }

        current
    }
}
