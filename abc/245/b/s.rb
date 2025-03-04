n = gets.to_i
a = gets.chomp.split.map(&:to_i)

a.max.times do |i|
  if a.include?(i) == false
    puts i
    break
  end
end
