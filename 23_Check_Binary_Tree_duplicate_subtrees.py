class Solution:
    def dupSub(self, root):
        seen_subtrees = set()

        def serialize_and_check_duplicate(node):
            if not node: return ''
            if not node.left and not node.right: return str(node.data)

            left_serialized = serialize_and_check_duplicate(node.left)
            if left_serialized == True:
                return True

            right_serialized = serialize_and_check_duplicate(node.right)
            if right_serialized == True:
                return True

            current_serialized = str(node.data)
            if left_serialized != '':
                current_serialized += 'l' + left_serialized
            if right_serialized != '':
                current_serialized += 'r' + right_serialized

            if current_serialized in seen_subtrees:
                return True

            seen_subtrees.add(current_serialized)
            return current_serialized

        return 1 if serialize_and_check_duplicate(root) == True else 0
