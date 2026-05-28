struct Node {
    children: [Option<usize>; 26],
    min_length: usize,
    index: usize
}

impl Node {
    fn new() -> Self {
        Node {
            children: [None; 26],
            min_length: usize::MAX,
            index: usize::MAX,
        }
    }
}

struct Trie {
    nodes: Vec<Node>
}

impl Solution {
    pub fn string_indices(words_container: Vec<String>, words_query: Vec<String>) -> Vec<i32> {
        fn insert(trie: &mut Trie, i: usize, words_container: &Vec<String>) {
            let s = &words_container[i];
            let mut cur = 0usize;
            if trie.nodes[0].min_length > s.len() {
                trie.nodes[0].min_length = s.len();
                trie.nodes[0].index = i;
            }
            for c in s.chars().rev() {
                let j = (c.to_ascii_lowercase() as u8 - 97) as usize;
                if trie.nodes[cur].children[j].is_none() {
                    trie.nodes.push(Node::new());
                    trie.nodes[cur].children[j] = Some(trie.nodes.len() - 1);
                }
                cur = trie.nodes[cur].children[j].unwrap();
                if trie.nodes[cur].min_length > s.len() {
                    trie.nodes[cur].min_length = s.len();
                    trie.nodes[cur].index = i;
                } else if trie.nodes[cur].min_length == s.len() {
                    trie.nodes[cur].index = trie.nodes[cur].index.min(i);
                }
            }
        }

        fn query(trie: &Trie, query: &str) -> usize {
            let mut cur = 0usize;
            for c in query.chars().rev() {
                let i = (c.to_ascii_lowercase() as u8 - 97) as usize;
                if trie.nodes[cur].children[i].is_none() {
                    return trie.nodes[cur].index;
                }
                cur = trie.nodes[cur].children[i].unwrap();
            }
            return trie.nodes[cur].index;
        }

        let mut trie = Trie {
            nodes: vec![Node::new()]
        };

        for i in 0..words_container.len() {
            insert(&mut trie, i, &words_container);
        }


        let mut ans = Vec::new();
        for q in words_query {
            ans.push(query(&trie, &q) as i32);
        }
        ans
    }
}
