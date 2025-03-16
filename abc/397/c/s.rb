n = gets.to_i
a = gets.chomp.split.map(&:to_i)

x = [a, [0] * n].transpose.to_h
x[a[0]] = 1
y = a.tally

ans = 1 + a[1..].uniq.size
anss = [2]

1.upto(n-2) do |i|
  aa = a[i]
  x[aa] += 1
  y[aa] -= 1
  ans += 1 if x[aa] == 1
  ans -= 1 if y[aa] == 0
  anss << ans
end

puts anss.max
