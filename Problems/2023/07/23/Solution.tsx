/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function allPossibleFBT(n: number): Array<TreeNode | null> {
  if (n % 2 === 0) {return [];}
  const FBT: Map<number, Array<TreeNode | null>> = new Map();
  FBT.set(1, [new TreeNode()]);
  for (let i = 3; i <= n; i += 2) {
    const arr = []
    for (let left = 1; left <= i - 2; left += 2) {
      const right = i - left - 1;
      for (const l of FBT.get(left)) {
        console.log(i, left, right);
        for (const r of FBT.get(right)) {
          const root = new TreeNode();
          root.left = l;
          root.right = r;
          arr.push(root);
        }
      }
    }
    FBT.set(i, arr);
  }
  return FBT.get(n);
};
