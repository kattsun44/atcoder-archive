h, w = gets.chomp.split.map(&:to_i)

s = h.times.map { gets.chomp.split("") }

a = []
h.times do |i|
  w.times do |j|
    if s[i][j] == "o"
      a << [i, j]
    end
  end
end

puts (a[1][0] - a[0][0]).abs + (a[1][1] - a[0][1]).abs
