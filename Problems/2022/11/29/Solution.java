class RandomizedSet {

    private int[] arr = new int[200000];
    private int size;
    private Map<Integer, Integer> index;
    private Random rand = new Random();

    public RandomizedSet() {
        this.index = new HashMap<>();
    }

    public boolean insert(int val) {
        if (index.containsKey(val)) {
            return false;
        }
        index.put(val, size);
        arr[size] = val;
        size++;
        return true;
    }

    public boolean remove(int val) {
        if (!index.containsKey(val) || size == 0) {
            return false;
        }
        int i = index.get(val);
        int j = size-1;
        index.put(arr[j], i);
        index.remove(arr[i]);
        arr[i] = arr[j];
        size--;
        return true;
    }

    public int getRandom() {
        return arr[rand.nextInt(size)];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
