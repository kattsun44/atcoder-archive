h, w = gets.chomp.split(" ").map(&:to_i)
arrays = h.times.map { gets.chomp.split(" ").map(&:to_i) }

arrays.transpose.each do |a|
  puts a.join(" ")
end
