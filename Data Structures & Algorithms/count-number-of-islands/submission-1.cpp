class Solution {
    int directions[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows=grid.size(),cols=grid[0].size();
        int islands=0;
        for(int i = 0 ; i < rows ; i++) {
            for(int j = 0 ; j < cols ; j++) {
                if (grid[i][j]=='1') {
                    bfs(grid,i,j);
                    islands++;
                }
            }
        }
        return islands;
    }
    void bfs(vector<vector<char>>& grid, int r, int c) {
        queue<pair<int,int>> q;
        grid[r][c]='0';
        q.push({r,c});

        while(!q.empty()) {
            auto node=q.front();
            int row=node.first, col=node.second;
            q.pop();
            for (int i = 0 ; i < 4 ; i++) {
                int nr = row + directions[i][0];
                int nc = col + directions[i][1];
                if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc]=='1') {
                    q.push({nr,nc});
                    grid[nr][nc]='0';
                }
            }
        }
    }
};
