n = gets.to_i
a = gets.chomp.split.map(&:to_i)

h = Hash.new(0)

a.each { h[_1] += 1}

max = h.select { _2 == 1 }.keys.max

puts max.nil? ? -1 : a.find_index(max) + 1
