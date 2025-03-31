n, w = gets.chomp.split.map(&:to_i)
a = gets.chomp.split.map(&:to_i)

puts (1..3).flat_map { a.combination(_1).to_a }.map(&:sum).uniq.count { _1 <= w }
