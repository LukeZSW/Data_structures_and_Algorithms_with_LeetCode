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
    void checkpath(TreeNode* root, int sum, int &flag) {
        if(root->left != NULL) {
            checkpath(root->left, sum - root->val, flag);
        }
        if(root->right != NULL) {
            checkpath(root->right, sum - root->val, flag);
        }
        if(root->left == NULL && root->right == NULL && sum == root->val) {
            flag = 1;
        }
    }
    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL)
            return false;
        int flag = 0;
        if(root->left != NULL) {
            checkpath(root->left, sum - root->val, flag);
        }
        if(root->right != NULL) {
            checkpath(root->right, sum - root->val, flag);
        }
        if(root->left == NULL && root->right == NULL && sum == root->val) {
            flag = 1;
        }
        if(flag == 1) {
            return true;
        } else {
            return false;
        }
    }
};