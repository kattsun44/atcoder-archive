H, W = gets.chomp.split.map(&:to_i)
R, C = gets.chomp.split.map(&:to_i)

ans = 0
ans += 1 if R > 1
ans += 1 if R < H
ans += 1 if C > 1
ans += 1 if C < W

puts ans
