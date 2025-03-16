n = gets.to_i
a = gets.chomp.split.map(&:to_i)

sum_l = [0] * n
sum_r = [0] * n

x = [a, [0] * n].transpose.to_h
y = [a, [0] * n].transpose.to_h

s = 0
n.times do |i|
  if x[a[i]] == 0
    x[a[i]] = 1
    s += 1
  end
  sum_l[i] = s
end

a_rev = a.reverse
s = 0
n.times do |i|
  if y[a_rev[i]] == 0
    y[a_rev[i]] = 1
    s += 1
  end
  sum_r[i] = s
end

puts [sum_l[...-1], sum_r.reverse[1..]].transpose.map(&:sum).max
