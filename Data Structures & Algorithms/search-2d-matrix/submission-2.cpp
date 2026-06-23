class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l_out=0;
        int r_out=matrix.size()-1;
        while (l_out<=r_out) {
            int m_out=l_out+((r_out-l_out)/2);
            if (target<matrix[m_out][0]) {
                r_out--;
            }
            else if (target>matrix[m_out][matrix[m_out].size()-1]) {
                l_out++;
            }
            else {
                int l_in=0;
                int r_in=matrix[m_out].size()-1;
                while (l_in<=r_in) {
                    int m_in=l_in+((r_in-l_in)/2);
                    if(target<matrix[m_out][m_in]) {
                        r_in--;
                    }
                    else if(target>matrix[m_out][m_in]) {
                        l_in++;
                    }
                    else {
                        return true;
                    }
                }
                return false;
            }
        }
        return false;
    }
};
