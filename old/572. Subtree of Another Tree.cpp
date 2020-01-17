572. Subtree of Another Tree/**
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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(s->val == t->val)
        {
            bool c1 = check(s->left, t->left);
            bool c2 = check(s->right, t->right);
            if(c1 && c2)
                return true;
        }
        if(s->left == NULL && s->right == NULL) {
            return false;
        }
        bool c3 = false;
        bool c4 = false;
        if(s->left != NULL)
        {
            c3 = isSubtree(s->left, t);
        }
        if(s->right != NULL)
        {
            c4 = isSubtree(s->right, t);
        }
        return c3 || c4;
    }
    
    bool check(TreeNode* s, TreeNode* t)
    {
        if(s == NULL && t == NULL)
            return true;
        if(s == NULL && t != NULL)
            return false;
        if(s != NULL && t == NULL)
            return false;
        if(s->val == t->val)
        {
            return check(s->left, t->left) && check(s->right, t->right);
        }
        else
        {
            return false;           
        }
    }
};