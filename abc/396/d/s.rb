n, m = gets.chomp.split.map(&:to_i)

# h = Hash.new{ |h, k| h[k] = [] }

# m.times do
#   u, v, w = gets.chomp.split.map(&:to_i)
#   h[u].push([v, w])
# end

# pp h

def dfs(pos, graph, visited, s, ans, m)
  visited[pos] = true
  graph[pos].each do |next_pos|
    s << next_pos[1]
    if pos == m
      ans << s.inject(:^)
      s = []
    end
    dfs(next_pos[0], graph, visited, s, ans, m) unless visited[next_pos[0]]
  end
end

s = []
ans = []
graph = Array.new(n+1) { [] }
visited = Array.new(n+1, false)
visited[0] = true

m.times do |i|
  u, v, w = gets.chomp.split.map(&:to_i)
  # 双方向に辺を張る
  graph[u] << [v, w]
  graph[v] << [u, w]
end

dfs(1, graph, visited, s, ans, m)

# pp [graph, visited]
pp ans
