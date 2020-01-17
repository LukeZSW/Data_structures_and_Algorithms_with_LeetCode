/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        unordered_map<TreeNode*, int> m;
        return dfs(root, m);
    }
    int dfs(TreeNode* root, unordered_map<TreeNode*, int> &m) {
        if(!root)
            return 0;
        if (m.find(root) != m.end()) 
            return m[root];
        int val = 0;
        if(root->left != NULL) {
            val += dfs(root->left->left, m) + dfs(root->left->right, m);
        } 
        if(root->right != NULL) {
            val += dfs(root->right->left, m) + dfs(root->right->right, m);
        }
        val = max(root->val + val, dfs(root->left, m) + dfs(root->right, m));
        m[root] = val;
        return val;
    }
};