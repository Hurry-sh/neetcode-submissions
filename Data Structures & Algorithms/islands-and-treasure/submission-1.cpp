class Solution {
public:
    int rows,cols;
    vector<vector<int>> directions = {{1,0},{-1,0},{0,1},{0,-1}};
    int inf = 2147483647; 

    int bfs(vector<vector<int>>& grid, int r, int c) {
        queue<pair<int,int>> q;
        q.push({r,c});
        vector<vector<bool>> visit(rows,vector<bool>(cols,false));
        visit[r][c]=true;
        int steps=0;

        while(!q.empty()) {
            int size = q.size();
            for(int i = 0 ; i < size ; i++) {
                auto [row,col] = q.front();
                q.pop();
                if(grid[row][col] == 0) {
                    return steps;
                }
                for(auto& dir : directions){
                    int nr = row + dir[0], nc = col + dir[1];
                    if (nr >= 0 && nr < rows && 
                    nc >= 0 && nc < cols && 
                    visit[nr][nc] == false && grid[nr][nc] != -1) {
                        visit[nr][nc] = true;
                        q.push({nr,nc});
                    }
                }
            }
            steps++;
        }
        return inf;
    }

    void islandsAndTreasure(vector<vector<int>>& grid) {
        rows = grid.size();
        cols=grid[0].size();
        for(int i = 0 ; i < rows ; i++){
            for(int j = 0 ; j < cols ; j++) {
                if(grid[i][j]==inf) {
                    grid[i][j]=bfs(grid,i,j);
                }
            }
        }   
    }
};
