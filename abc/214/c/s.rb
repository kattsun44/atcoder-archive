n = gets.chomp.to_i
s = gets.chomp.split(" ").map(&:to_i)
t = gets.chomp.split(" ").map(&:to_i)
ans = [0] * n

start = t.index(t.min)

n.times do |index|
  i = (start + index) % n
  if i.zero?
    ans[i] = t[i]
  else
    ans[i] = [t[i], ans[i-1] + s[i-1]].min
  end
end

puts ans
