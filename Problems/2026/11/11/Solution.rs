impl Solution {
    pub fn minimum_cost(cost1: i32, cost2: i32, cost_both: i32, need1: i32, need2: i32) -> i64 {
        let (cost1, cost2, cost_both, mut need1, mut need2) = (cost1 as i64, cost2 as i64, cost_both as i64, need1 as i64, need2 as i64);
        if cost1 >= cost_both && cost2 >= cost_both {
            return cost_both * need1.max(need2);
        }
        let mut total = 0_i64;
        if cost1 + cost2 >= cost_both {
            let count = need1.min(need2);
            total += cost_both * count;
            need1 -= count;
            need2 -= count;
        }
        total += need1 * cost1.min(cost_both);
        total += need2 * cost2.min(cost_both);
        total
    }
}
