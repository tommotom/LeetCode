class Obj implements Comparable<Obj> {

    String key;
    String value;
    int timestamp;

    public Obj(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }

    public int compareTo(Obj another) {
        return Integer.compare(this.timestamp, another.timestamp);
    }
}

class TimeMap {

    Map<String, List<Obj>> map = new HashMap<>();

    public TimeMap() {
    }

    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)) {
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(new Obj(value, timestamp));
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }
        List<Obj> list = map.get(key);
        int l = 0, r = list.size();
        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m).timestamp <= timestamp) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        if (l == 0) {
            return "";
        }

        return list.get(l-1).value;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
