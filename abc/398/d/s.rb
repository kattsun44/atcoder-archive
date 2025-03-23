N, R, C = gets.chomp.split.map(&:to_i)
S = gets.chomp.chars
ans = []

# 焚き火が移動する方向
direct = { "N" => [-1, 0], "E" => [0, 1], "S" => [1, 0], "W" => [0, -1] }

# 高橋君の位置ログ
log = {}
log[[R, C]] = true

# 焚き火の初期位置
r = c = 0

S.each do |s|
  # 焚き火の位置の更新
  dr, dc = direct[s]
  r += dr
  c += dc

  # Q: なぜ更新後の焚き火の位置が高橋くんの過去いた位置にくると 1 になる？
  ans << (log[[r, c]] ? 1 : 0)

  log[[R + r, C + c]] = true
end

puts ans.join
