
use std::sync::OnceLock;

struct PrimeSieve {
    is_prime: Vec<bool>,
    prime_factors: Vec<Vec<usize>>,
}

static SIEVE: OnceLock<PrimeSieve> = OnceLock::new();

// Compute prime sieve exactly once
fn get_sieve() -> &'static PrimeSieve {
    SIEVE.get_or_init(|| {
        let max_nr = 1000000usize;
        let mut is_prime = vec![true; max_nr+1];
        let mut prime_factors = vec![vec![]; max_nr+1];
        is_prime[0] = false;
        is_prime[1] = false;
        for p in 2..=max_nr {
            if is_prime[p] {
                for k in (2*p..=max_nr).step_by(p) {
                    is_prime[k] = false;
                    prime_factors[k].push(p);
                }
            }
        }
        PrimeSieve{is_prime, prime_factors}
    })
}

impl Solution {

    pub fn min_jumps(nums: Vec<i32>) -> i32 {
        use std::collections::{HashSet, VecDeque, HashMap};
        let n = nums.len();
        // Step 1: find all prime numbers in [1, m], as well as all prime factors for composite values
        //         We need to make sure this is only performed once.
        let sieve = get_sieve();
        // Step 2: map all prime numbers to all indices where nums[j] is divisible by the prime
        let mut all_indices: HashMap::<usize, Vec<usize>> = HashMap::new();
        for (i, x) in nums.iter().enumerate() {
            let mut x = *x as usize;
            if sieve.is_prime[x] {
                all_indices.entry(x).or_insert(vec![]).push(i);
            } else {
                for p in sieve.prime_factors[x].iter() {
                    all_indices.entry(*p).or_insert(vec![]).push(i);
                }
            }
        }

        // Step 3: run breadth-first search

        let mut q = VecDeque::new();
        let mut primes_found = HashSet::new();
        q.push_back((0, 0));
        let mut visited = vec![false; n];
        while let Some((index, nb_steps)) = q.pop_front() {
            if visited[index] {
                continue;
            }
            visited[index] = true;
            if index + 1 == n {
                return nb_steps;
            }
            if index > 0 && !visited[index-1] {
                q.push_back((index-1, nb_steps+1));
            }
            if !visited[index+1]{
                q.push_back((index+1, nb_steps+1));
            }
            let p = nums[index] as usize;
            if sieve.is_prime[p] {
                if primes_found.contains(&p){
                    continue;
                }
                primes_found.insert(p);
                for j in all_indices.get(&p).unwrap() {
                    if !visited[*j]{
                        q.push_back((*j, nb_steps+1));
                    }
                }
            }

        }

        -1 // should not be reached
    }
}
