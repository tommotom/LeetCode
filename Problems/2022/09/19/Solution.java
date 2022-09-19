class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> contentToPath = new HashMap<>();
        for (String path : paths) {
            String[] pathAndFile = path.split(" ");
            for (int i = 1; i < pathAndFile.length; i++) {
                String[] nameAndContent = pathAndFile[i].split("[()]");
                String content = nameAndContent[1];
                if (!contentToPath.containsKey(content)) {
                    contentToPath.put(content, new ArrayList<>());
                }
                String filePath = pathAndFile[0] + "/" + nameAndContent[0];
                contentToPath.get(content).add(filePath);
            }
        }

        List<List<String>> ans = new ArrayList<>();
        for (String key : contentToPath.keySet()) {
            if (contentToPath.get(key).size() > 1) {
                ans.add(contentToPath.get(key));
            }
        }
        return ans;
    }
}
