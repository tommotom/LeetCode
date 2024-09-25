class Node {
    isWord: number;
    children: Map<String, Node>;

    constructor() {
        this.isWord = 0;
        this.children = new Map();
    }
}

function sumPrefixScores(words: string[]): number[] {
    const root = new Node();
    for (const word of words) {
        let node = root;
        for (const w of word.split('')) {
            if (!node.children.has(w)) {
                node.children.set(w, new Node())
            }
            node = node.children.get(w);
            node.isWord += 1;
        }
    }

    const ans = [];
    for (const word of words) {
        let node = root;
        let count = 0;
        for (const w of word.split('')) {
            node = node.children.get(w);
            count += node.isWord;
        }
        ans.push(count);
    }

    return ans;
};
