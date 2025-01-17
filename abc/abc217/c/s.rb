n = gets.chomp.to_i
p = gets.chomp.split(" ").map(&:to_i)

q = [0] * n

p.each_with_index do |pp, i|
  q[pp - 1] = i + 1
end

puts q.join(" ")
