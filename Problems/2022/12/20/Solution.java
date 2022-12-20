class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        Stack<Integer> st = new Stack<>();
        st.push(0);
        while (!st.isEmpty()) {
            int i = st.pop();
            for (int j : rooms.get(i)) {
                if (!visited.contains(j)) {
                    visited.add(j);
                    st.push(j);
                }
            }
        }

        return visited.size() == rooms.size();
    }
}
