x1, y1 = gets.chomp.split.map(&:to_i)
x2, y2 = gets.chomp.split.map(&:to_i)
x3, y3 = gets.chomp.split.map(&:to_i)

puts [[x1, x2, x3].tally.select { _2 == 1 }.keys.first, [y1, y2, y3].tally.select { _2 == 1 }.keys.first].join(" ")
