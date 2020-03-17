package BOJ

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val (N, D, M) = br.readLine()!!.split(" ").map { it.toInt() }
    var money = M
    var stocks = Array(N) { Array(D) { 0 } }
    for (i in 0 until N) {
        br.readLine().split(" ").forEachIndexed { j, e ->
            stocks[i][j] = e.toInt()
        }
    }

    for (day in 0 until D-1) {
        val dp = Array(money + 1) { 0 }
        for (i in 0 until N) {
            val cur = stocks[i][day]
            val next = stocks[i][day+1]
            val diff = next - cur
            for (k in 0..money-cur) {
                dp[k+cur] = max(dp[k+cur], dp[k] + diff)
            }
        }
        money += dp[money]

    }
    br.close()
    println(money)
}

fun max(a: Int, b: Int) = if (a > b) a else b

/*
씨쁠쁠로 바꾸니까 되더라
#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXS 51
#define MAXD 11

static int prices[MAXD][MAXS];
int dp[500001];

int main()
{
    int S, D, M;

    scanf("%d %d %d", &S, &D, &M);
    for (int i = 0; i < S; i++)
        for (int j = 0; j < D; j++)
            scanf("%d", &prices[j][i]);

    for (int i = 1; i < D; i++)
    {
        for (int j = 0; j <= M; j++)
            dp[j] = 0;
        for (int s = 0; s < S; s++)
        {
            int cur = prices[i - 1][s];
            int diff = prices[i][s] - cur;
            for (int k = 0; k <= M-cur; k++)
            {
                if (dp[k+cur] < dp[k] + diff) dp[k+cur] = dp[k] + diff;
            }
        }
        M += dp[M];
    }
    printf("%d", M);
    return 0;
} 
*/