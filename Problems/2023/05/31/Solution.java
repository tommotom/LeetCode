class UndergroundSystem {

    private final Map<Integer, Pair<String, Integer>> in = new HashMap<>();
    private final Map<Pair<String, String>, Long> sum = new HashMap<>();
    private final Map<Pair<String, String>, Integer> count = new HashMap<>();

    public UndergroundSystem() {
    }

    public void checkIn(int id, String stationName, int t) {
        in.put(id, new Pair(stationName, t));
    }

    public void checkOut(int id, String stationName, int t) {
        Pair<String, Integer> from = in.get(id);
        Pair<String, String> key = new Pair(from.getKey(), stationName);
        sum.put(key, sum.getOrDefault(key, 0L) + t - from.getValue());
        count.put(key, count.getOrDefault(key, 0) + 1);
    }

    public double getAverageTime(String startStation, String endStation) {
        Pair<String, String> key = new Pair(startStation, endStation);
        return (double) sum.get(key) / count.get(key);
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
