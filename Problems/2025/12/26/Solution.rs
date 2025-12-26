impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let customers: Vec<char> = customers.chars().collect();
        let mut penalty = 0;
        for c in &customers {
            if *c == 'Y' {
                penalty += 1;
            }
        }

        let mut min = penalty;
        let mut ans = 0;
        for i in 0..customers.len() {
            if customers[i] == 'Y' {
                penalty -= 1;
            } else {
                penalty += 1;
            }
            if min > penalty {
                min = penalty;
                ans = i + 1;
            }
        }
        ans as i32
    }
}
