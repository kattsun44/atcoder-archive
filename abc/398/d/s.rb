N, R, C = gets.chomp.split.map(&:to_i)
S = gets.chomp.chars
ans = []

direct = { "N" => [-1, 0], "E" => [0, 1], "S" => [1, 0], "W" => [0, -1] }

log = {}
log[[R, C]] = true

rc = [0, 0]
S.each_with_index do |s, i|
  rc = [rc, direct[s]].transpose.map(&:sum)
  ans << (log[rc] ? 1 : 0)
  log[[[R, C], rc].transpose.map(&:sum)] = true
end

puts ans.join
