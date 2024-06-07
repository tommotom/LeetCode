class Node {
    val: string;
    isRoot: boolean;
    children: Map<string, Node>;
    constructor(val: string) {
        this.val = val;
        this.isRoot = false;
        this.children = new Map();
    }
}

function replaceWords(dictionary: string[], sentence: string): string {
    const trie = new Node("");
    for (const word of dictionary) {
        let cur = trie;
        for (const w of word) {
            if (!cur.children.has(w)) {
                cur.children.set(w, new Node(w));
            }
            cur = cur.children.get(w);
        }
        cur.isRoot = true;
    }

    const replace = word => {
        let cur = trie;
        const path = [];
        for (const w of word) {
            if (!cur.children.has(w)) {
                break;
            }
            cur = cur.children.get(w);
            path.push(w);
            if (cur.isRoot) {
                return path.join('');
            }
        }
        return word;
    }

    return sentence.split(' ').map(word => replace(word)).join(' ');
};
