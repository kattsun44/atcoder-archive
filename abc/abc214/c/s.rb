n = gets.chomp.to_i
s = gets.chomp.split(" ").map(&:to_i)
t = gets.chomp.split(" ").map(&:to_i)
ans = [0] * n

start = t.index(t.min)

n.times do |i|
  index = (start + i) % n
  if i.zero?
    ans[index] = t[index]
  else
    ans[index] = [t[index], ans[index-1] + s[index-1]].min
  end
end

puts ans
