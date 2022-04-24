class CheckIn {
  public String stationName;
  public int time;

  public CheckIn(String stationName, int time) {
    this.stationName = stationName;
    this.time = time;
  }
}

class History {
  public long total;
  public long passengers;

  public double average() {
    if (passengers == 0) {
      return 0;
    }
    return (double) this.total / this.passengers;
  }
}


class UndergroundSystem {

  private Map<Integer, CheckIn> boarding;
  private Map<String, Map<String, History>> stat;


  public UndergroundSystem() {
    boarding = new HashMap<>();
    stat = new HashMap<>();
  }

  public void checkIn(int id, String stationName, int t) {
    boarding.put(id, new CheckIn(stationName, t));
  }

  public void checkOut(int id, String stationName, int t) {
    CheckIn in = boarding.get(id);
    if (!stat.containsKey(in.stationName)) {
      stat.put(in.stationName, new HashMap<>());
    }
    if (!stat.get(in.stationName).containsKey(stationName)) {
      stat.get(in.stationName).put(stationName, new History());
    }
    stat.get(in.stationName).get(stationName).total += t - in.time;
    stat.get(in.stationName).get(stationName).passengers++;
  }

  public double getAverageTime(String startStation, String endStation) {
    return stat.get(startStation).get(endStation).average();
  }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
