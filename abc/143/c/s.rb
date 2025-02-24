n = gets.to_i
s = gets.chomp

ans = []
n.times do |i|
  now, nx = s[i], s[i+1]
  ans << now if now != nx
end

puts ans.size
