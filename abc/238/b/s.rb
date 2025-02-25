n = gets.to_i
a = gets.chomp.split(" ").map(&:to_i)

angles = [0, 360]

n.times do |i|
  angles << a[0..i].sum % 360
end

puts angles.sort.each_cons(2).map { _2 - _1 }.max
