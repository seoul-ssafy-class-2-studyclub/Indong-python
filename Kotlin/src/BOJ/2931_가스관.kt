package BOJ

import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val dy = arrayOf(-1, 0, 1, 0)
    val dx = arrayOf(0, 1, 0, -1)
    val pipeFrom = hashMapOf<Char, Array<Int>>(
        '|' to arrayOf(0, 2),
        '-' to arrayOf(1, 3),
        '+' to arrayOf(0, 1, 2, 3),
        '1' to arrayOf(1, 2),
        '2' to arrayOf(0, 1),
        '3' to arrayOf(0, 3),
        '4' to arrayOf(2, 3)
    )
    val pipeTo = hashMapOf<Int, Array<Char>>(
        0 to arrayOf('|', '+', '1', '4'),
        1 to arrayOf('-', '+', '3', '4'),
        2 to arrayOf('|', '+', '2', '3'),
        3 to arrayOf('-', '+', '1', '2')
    )
    val pipeShape = hashMapOf<Int, Char>(
        5 to '|',
        10 to '-',
        15 to '+',
        6 to '1',
        3 to '2',
        9 to '3',
        12 to '4'
    )

    val br= BufferedReader(InputStreamReader(System.`in`))
    val (R, C) = br.readLine()!!.split(" ").map { it.toInt() }
    var board = Array(R) { Array(C) { '0' } }
    for (i in 0 until R) {
        var j = 0
        br.readLine()!!.forEach { board[i][j++] = it.toChar() }
    }
    var visit = Array(R) { Array(C) { false } }

    var flag = false
    var result: String = ""

    fun checkRange(y: Int, x: Int): Boolean {
        return y in 0 until R && x in 0 until C
    }

    fun dfs(y: Int, x: Int) {
        if (flag) return

        if (board[y][x] == '.') {
            var pipeBit = 0
            for (i in 0..3) {
                val yi = y + dy[i]
                val xi = x + dx[i]
                if (checkRange(yi, xi) && board[yi][xi] != '.' && pipeTo[i]!!.contains(board[yi][xi])) pipeBit += 1 shl i
            }
            result = "${y+1} ${x+1} ${pipeShape[pipeBit]}"
            flag = true
            return
        }

        pipeFrom[board[y][x]]!!.forEach {
            val yi = y + dy[it]
            val xi = x + dx[it]
            when {
                !checkRange(yi, xi) || board[yi][xi] == 'M' || board[yi][xi] == 'Z' -> {}
                !(visit[yi][xi]) -> {
                    visit[yi][xi] = true
                    dfs(yi, xi)
                    visit[yi][xi] = false
                }
            }
        }
    }

    first@ for (r in 0 until R) {
        for (c in 0 until C) {
            if (board[r][c] == 'M') {
                for (i in 0..3) {
                    val ri = r + dy[i]
                    val ci = c + dx[i]
                    if (checkRange(ri, ci) && board[ri][ci] in pipeFrom.keys) dfs(ri, ci)
                }
                break@first
            }
        }
    }

    println(result)
}