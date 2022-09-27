class Solution {
    public String pushDominoes(String dominoes) {
        Map<Integer, Character> toward = new HashMap<>();
        for (int i = 0; i < dominoes.length(); i++) {
            char c = dominoes.charAt(i);
            if (c == 'L' && i > 0 && dominoes.charAt(i-1) == '.') {
                if (toward.containsKey(i-1)) {
                    toward.remove(i-1);
                } else {
                    toward.put(i-1, 'L');
                }
            } else if (c == 'R' && i+1 < dominoes.length() && dominoes.charAt(i+1) == '.') {
                toward.put(i+1, 'R');
            }
        }


        char[] arr = dominoes.toCharArray();
        while (toward.size() > 0) {
            Map<Integer, Character> next = new HashMap<>();
            for (int i : toward.keySet()) {
                char c = toward.get(i);
                arr[i] = c;
                if (next.containsKey(i)) {
                    next.remove(i);
                }
                if (c == 'L' && i > 0 && arr[i-1] == '.') {
                    if (next.containsKey(i-1)) {
                        next.remove(i-1);
                    } else {
                        next.put(i-1, 'L');
                    }
                } else if (c == 'R' && i+1 < dominoes.length() && arr[i+1] == '.') {
                    if (next.containsKey(i+1)) {
                        next.remove(i+1);
                    } else {
                        next.put(i+1, 'R');
                    }
                }
            }
            toward = next;
        }

        return new String(arr);
    }
}
