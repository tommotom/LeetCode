class Count implements Comparable<Count> {
    final char c;
    int count;

    public Count(char c) {
        this.c = c;
    }

    public int compareTo(Count a) {
        return Integer.compare(a.count, this.count);
    }
}

class Solution {
    public String frequencySort(String s) {
        Count[] arr = new Count[80];
        for (char c : s.toCharArray()) {
            int i = c - '0';
            if (arr[i] == null) {
                arr[i] = new Count(c);
            }
            arr[i].count++;
        }

        Arrays.sort(arr, new Comparator<Count>() {
            @Override
            public int compare(Count o1, Count o2) {
                if (o1 == null && o2 == null) {
                    return 0;
                }
                if (o1 == null) {
                    return 1;
                }
                if (o2 == null) {
                    return -1;
                }
                return o1.compareTo(o2);
            }});

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 80; i ++) {
            if (arr[i] == null) {continue;}
            Count c = arr[i];
            for (int j = 0; j < c.count; j++) {
                sb.append(c.c);
            }
        }

        return sb.toString();
    }
}
