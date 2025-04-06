-- Select the 'id' column from the Tree table
SELECT id, 
  -- Check if the 'p_id' is NULL to identify the Root node
  CASE 
    WHEN p_id IS NULL THEN 'Root'  -- Node with no parent (p_id is NULL) is a Root
    -- Check if the node is a Leaf node
    WHEN id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'  -- Node that is not a parent (not found in p_id of any row) is a Leaf
    -- Otherwise, the node is considered an Inner node
    ELSE 'Inner'  -- Node that is neither Root nor Leaf, must be Inner
  END as type 
-- From the Tree table
FROM Tree;
