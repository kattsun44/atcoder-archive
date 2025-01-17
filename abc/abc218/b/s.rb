p = gets.chomp.split(" ").map(&:to_i)
h = [(1..26).to_a, ("a".."z").to_a].transpose.to_h

puts p.map { h[_1] }.join
