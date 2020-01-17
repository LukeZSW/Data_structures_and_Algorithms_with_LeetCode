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
    int pathSum(TreeNode* root, int sum) {
        if(!root)
            return 0;
        int ans = path(root, 0, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
        return ans;
    }
    int path(TreeNode* root, int pre, int sum)
    {
        if(!root)
            return 0;
        int cur = pre + root->val;
        return (cur == sum) + path(root->left, cur, sum) + path(root->right, cur, sum);
    }
};

//DFS
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
    void dfs(TreeNode* root, int sum, int& count, vector<int>& subres){
        subres.push_back(root->val);
        int subsum = 0;
        for (auto it = subres.rbegin(); it != subres.rend(); ++it) {
            subsum += (*it);
            if (subsum == sum) count++;
        }
        
        if (root->left) dfs(root->left, sum, count, subres);
        if (root->right) dfs(root->right, sum, count, subres);
        subres.pop_back();
    }
    
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL) return 0;
        vector<int> subres;
        int count = 0;
        dfs(root, sum, count, subres);
        return count;
    }
};