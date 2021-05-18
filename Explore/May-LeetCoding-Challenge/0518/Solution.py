class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_file_path = collections.defaultdict(list)
        for path in paths:
            arr = path.split(" ")
            for file in arr[1:]:
                name, _, content = file.partition("(")
                content_to_file_path[content[:-1]].append(arr[0]+"/"+name)
        return [arr for arr in content_to_file_path.values() if len(arr) > 1]
