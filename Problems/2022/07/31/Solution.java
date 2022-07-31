class NumArray {

    private int[] fen;
    private int[] arr;

    public NumArray(int[] nums) {
        arr = new int[nums.length];
        fen = new int[nums.length+2];
        for (int i = 0; i < nums.length; i++) {
            update(i, nums[i]);
        }
    }

    public void update(int index, int val) {
        int org = arr[index];
        arr[index] = val;
        add(index, val - org);
    }

    private void add(int index, int val) {
        index++;
        while (index < fen.length) {
            fen[index] += val;
            index += lsb(index);
        }
    }

    public int sumRange(int left, int right) {
        return sum(right+1) - sum(left);
    }

    private int sum(int right) {
        int sum = 0;
        while (right > 0) {
            sum += fen[right];
            right -= lsb(right);
        }
        return sum;
    }

    private int lsb(int num) {
        return num & (-num);
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */
