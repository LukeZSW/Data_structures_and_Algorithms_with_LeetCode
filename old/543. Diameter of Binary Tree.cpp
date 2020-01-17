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
    int answer;
    int diameterOfBinaryTree(TreeNode* root) {
        answer = 1;
        depth(root);
        return answer - 1;
    }
    int depth(TreeNode* root) {
        if(!root)
            return 0;
        int l = depth(root->left);
        int r = depth(root->right);
        answer = max(answer, l + r + 1);
        return max(l, r) + 1;
    }
};