n, m = gets.chomp.split(" ").map(&:to_i)
s = gets.chomp.split(" ")
t = gets.chomp.split(" ")

check = s.map { [_1, "No"] }.to_h

t.each { |tt| check[tt] = "Yes" }

puts check.values
