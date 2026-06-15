impl Solution {
    pub fn pair_sum(head: Option<Box<ListNode>>) -> i32 {
        let vals: Vec<_> = std::iter::successors(head.as_ref(), |n| n.next.as_ref())
            .map(|n| n.val)
            .collect();

        vals.iter()
            .zip(vals.iter().rev())
            .take(vals.len() >> 1)
            .fold(0, |max, (l, r)| max.max(l + r))
    }
}
