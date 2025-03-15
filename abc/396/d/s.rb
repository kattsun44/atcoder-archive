# https://atcoder.jp/contests/abc396/tasks/abc396_d
# D - Minimum XOR Path

# ### 問題文
#
# 頂点に 1 から N の、辺に 1 から M の番号がついた N 頂点 M 辺の単純連結無向グラフが与えられます。
# 辺 ii は頂点 ui と頂点 vi を結んでおり、ラベル wi が付けられています。
# 頂点 1 から頂点 N への単純パス（同じ頂点を 2 度以上通らないパス）のうち、パスに含まれる辺につけられたラベルの総 XOR としてあり得る最小値を求めてください。

N, M = gets.chomp.split.map(&:to_i)

# 単純パスを全部列挙するために DFS を用いる
def dfs(pos, graph, visited, xor)
  visited[pos] = true # 頂点を訪問済みにする

  $ans = [$ans, xor].min if pos == N

  graph[pos].each { |v, w| dfs(v, graph, visited, xor ^ w) unless visited[v] }

  visited[pos] = false # 訪問済みを解除する
end

$ans = 1 << 60
graph = Array.new(N+1) { [] }
visited = Array.new(N+1) { false }
visited[0] = true #不使用

M.times do
  u, v, w = gets.chomp.split.map(&:to_i)
  # 双方向に辺を張る
  graph[u] << [v, w]
  graph[v] << [u, w]
end

dfs(1, graph, visited, 0)

pp $ans
