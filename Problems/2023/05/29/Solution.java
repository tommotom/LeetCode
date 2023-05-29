class Vacancy {
    private final Map<CarType, Integer> vacancy = new HashMap<>();

    void addVacancy(CarType carType, int count) {
        vacancy.put(carType, vacancy.getOrDefault(carType, 0) + count);
    }

    boolean hasVacancy(CarType carType) {
        return vacancy.getOrDefault(carType, 0) > 0;
    }

    void add(CarType carType) {
        vacancy.put(carType, vacancy.get(carType) - 1);
    }
}

enum CarType {
    BIG(1),
    MEDIUM(2),
    SMALL(3);

    private final int id;

    private CarType(final int id) {
        this.id = id;
    }

    int getId() {
        return id;
    }

    static CarType valueOf(final int id) {
        for (CarType type : values()) {
            if (type.getId() == id) {
                return type;
            }
        }
        throw new IllegalArgumentException("no such carType object for the id: " + id);
    }
}

class ParkingSystem {

    private final Vacancy vacancy;

    public ParkingSystem(int big, int medium, int small) {
        vacancy = new Vacancy();
        vacancy.addVacancy(CarType.BIG, big);
        vacancy.addVacancy(CarType.MEDIUM, medium);
        vacancy.addVacancy(CarType.SMALL, small);
    }

    public boolean addCar(int carType) {
        CarType c = CarType.valueOf(carType);
        if (!vacancy.hasVacancy(c)) {return false;}
        vacancy.add(c);
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
