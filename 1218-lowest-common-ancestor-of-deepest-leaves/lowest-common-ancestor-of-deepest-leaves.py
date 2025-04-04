class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Finds the lowest common ancestor (LCA) of the deepest leaves in a binary tree.
        
        For each node, the helper function returns a tuple:
          (max_depth_from_node, lca_of_deepest_leaves_in_subtree)
        """
        def compute_depth_and_lca(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            # Base case: An empty node contributes a depth of 0 and has no LCA.
            if not node:
                return (0, None)
            
            # Recursively compute depth and LCA for the left and right subtrees.
            left_depth, left_lca = compute_depth_and_lca(node.left)
            right_depth, right_lca = compute_depth_and_lca(node.right)
            
            # If both subtrees have the same depth, the current node is the common ancestor.
            if left_depth == right_depth:
                return (left_depth + 1, node)
            # If the left subtree is deeper, propagate its LCA.
            elif left_depth > right_depth:
                return (left_depth + 1, left_lca)
            # Otherwise, the right subtree is deeper, so propagate its LCA.
            else:
                return (right_depth + 1, right_lca)

        # The LCA of the deepest leaves is the second element of the tuple returned from the helper.
        return compute_depth_and_lca(root)[1]
