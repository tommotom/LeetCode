impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        operations.iter().map(|o| if o == "X++" || o == "++X" {1} else {-1}).sum()
    }
}
