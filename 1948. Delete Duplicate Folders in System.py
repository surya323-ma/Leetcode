Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.
For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.
For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z
However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.
Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
rom collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.name = ""
        self.serial = ""
        self.is_deleted = False

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = TrieNode()
        
        # Build trie
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    child = TrieNode()
                    child.name = folder
                    node.children[folder] = child
                node = node.children[folder]

        # Map serialized subtree → list of nodes
        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                node.serial = ""
                return ""
            items = []
            for child in sorted(node.children.values(), key=lambda x: x.name):
                items.append(f"{child.name}({serialize(child)})")
            node.serial = "".join(items)
            serial_map[node.serial].append(node)
            return node.serial

        serialize(root)

        # Mark duplicates
        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.is_deleted = True

        # Collect surviving paths
        ans = []

        def collect(node, path):
            for child in node.children.values():
                if not child.is_deleted:
                    new_path = path + [child.name]
                    ans.append(new_path)
                    collect(child, new_path)

        collect(root, [])
        return ans
