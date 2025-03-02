n = gets.to_i
a = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map(&:to_i)

puts [a, b].transpose.count { _1[0] == _1[1] }
puts a.each_with_index.count { |e, i| (b[0...i] + b[i+1...n]).include?(e) }
