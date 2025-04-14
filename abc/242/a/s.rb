a, b, c, x = gets.chomp.split.map(&:to_i)

p = if x <= a
  1
  elsif x > b
    0
  else
    c * 1.0 / (b - a)
  end

puts p
