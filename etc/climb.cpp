#include <bits/stdc++.h>
using namespace std;

int main()
{
    // freopen("input.txt", "r", stdin);

    int T;
    cin >> T;
    while (T--)
    {
        int N;
        cin >> N;

        vector<vector<char>> m(N, vector<char>(N));
        vector<vector<int>> ans(N, vector<int>(N, 0));

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                char c;
                cin >> c;
                m[i][j] = c;
            }
        }

        queue<pair<int, int>> q;
        ans[N - 1][0] = 1;
        q.push({N - 1, 0});

        while(!q.empty())
        {
            int cur_y = q.front().first;
            int cur_x = q.front().second;
            int step = ans[cur_y][cur_x];
            q.pop();

            // 1번
            //상
            if (cur_y > 0 && m[cur_y - 1][cur_x] == 'H' && ans[cur_y - 1][cur_x] == 0)
            {
                ans[cur_y - 1][cur_x] = step + 1;
                q.push({cur_y - 1, cur_x});
            }
            //하
            if (cur_y < N - 1 && m[cur_y + 1][cur_x] == 'H' && ans[cur_y + 1][cur_x] == 0)
            {
                ans[cur_y + 1][cur_x] = step + 1;
                q.push({cur_y + 1, cur_x});
            }
            //좌
            if (cur_x > 0 && m[cur_y][cur_x - 1] == 'H' && ans[cur_y][cur_x - 1] == 0)
            {
                ans[cur_y][cur_x - 1] = step + 1;
                q.push({cur_y, cur_x - 1});
            }
            //우
            if (cur_x < N - 1 && m[cur_y][cur_x + 1] == 'H' && ans[cur_y][cur_x + 1] == 0)
            {
                ans[cur_y][cur_x + 1] = step + 1;
                q.push({cur_y, cur_x + 1});
            }
            // 2번

            //좌로 2칸
            if (cur_y > 0 && cur_x - 2 >= 0)
            {
                if (m[cur_y][cur_x - 1] == '.' && m[cur_y][cur_x - 2] == 'H' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x - 1] == '.' && m[cur_y - 1][cur_x - 2] == '.' && ans[cur_y][cur_x-2] == 0)
                {
                    ans[cur_y][cur_x - 2] = step + 1;
                    q.push({cur_y, cur_x - 2});
                }
            }
            //우로 2칸
            if (cur_y > 0 && cur_x + 2 <= N - 1)
            {
                if (m[cur_y][cur_x + 1] == '.' && m[cur_y][cur_x + 2] == 'H' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x + 1] == '.' && m[cur_y - 1][cur_x + 2] == '.' && ans[cur_y][cur_x + 2] == 0)
                {
                    ans[cur_y][cur_x + 2] = step + 1;
                    q.push({cur_y, cur_x + 2});
                }
            }
            //좌로 3칸
            if (cur_y > 0 && cur_x - 3 >= 0)
            {
                if (m[cur_y][cur_x - 2] == '.' && m[cur_y][cur_x - 1] == '.' && m[cur_y][cur_x - 3] == 'H' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x - 1] == '.' && m[cur_y - 1][cur_x - 2] == '.' && m[cur_y - 1][cur_x - 3] == '.' && ans[cur_y][cur_x - 3]==0)
                {
                    ans[cur_y][cur_x - 3] = step + 1;
                    q.push({cur_y, cur_x - 3});
                }
            }

            //우로 3칸
            if (cur_y > 0 && cur_x + 3 >= 0)
            {
                if (m[cur_y][cur_x + 2] == '.' && m[cur_y][cur_x + 1] == '.' && m[cur_y][cur_x + 3] == 'H' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x + 1] == '.' && m[cur_y - 1][cur_x + 2] == '.' && m[cur_y - 1][cur_x + 3] == '.' && ans[cur_y][cur_x + 3] == 0)
                {
                    ans[cur_y][cur_x + 3] = step + 1;
                    q.push({cur_y, cur_x + 3});
                }
            }

            // 3번
            if (cur_y >= 2 && m[cur_y - 1][cur_x] == '.' && m[cur_y - 2][cur_x] == 'H' && ans[cur_y - 2][cur_x] ==0)
            {
                ans[cur_y - 2][cur_x] = step + 1;
                q.push({cur_y - 2, cur_x});
            }

            // 4번

            if (cur_y - 1 >= 0 && cur_x - 1 >= 0 && m[cur_y][cur_x - 1] == '.' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x - 1] == 'H' && ans[cur_y - 1][cur_x - 1] ==0)
            {
                ans[cur_y - 1][cur_x - 1] = step + 1;
                q.push({cur_y - 1, cur_x - 1});
            }

            // 5번
            if (cur_y - 1 >= 0 && cur_x + 1 < N && m[cur_y][cur_x + 1] == '.' && m[cur_y - 1][cur_x] == '.' && m[cur_y - 1][cur_x + 1] == 'H' && ans[cur_y - 1][cur_x + 1] == 0)
            {
                ans[cur_y - 1][cur_x + 1] = step + 1;
                q.push({cur_y - 1, cur_x + 1});
            }
        }

        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                if(ans[i][j] == 0 && m[i][j] == 'H')
                {
                    ans[i][j] = -1;
                }
            }
        }

        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                cout << ans[i][j] << " ";
            }
            cout << endl;
        }
    }
}