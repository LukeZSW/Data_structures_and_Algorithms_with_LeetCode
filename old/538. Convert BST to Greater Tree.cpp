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
    int temp = 0;
    TreeNode* convertBST(TreeNode* root) {
        if(!root)
            return NULL;
        if(root->right != NULL)
            convertBST(root->right);
        root->val += temp;
        temp = root->val;
        if(root->left != NULL)
            convertBST(root->left);
        return root;
    }
};
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        if (!root)
            return NULL;
        stack<TreeNode *> st;
        st.push(root);
        TreeNode * temp = root->right;
        int sum = 0;
        while(!st.empty() || temp){
            while(temp){
                st.push(temp);
                temp = temp->right;
            }
            temp = st.top();
            st.pop();
            sum += temp->val;
            temp->val = sum;
            temp = temp->left;
        }
        return root;
    }
};