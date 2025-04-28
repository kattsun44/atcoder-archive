n = gets.to_i
a = gets.chomp.split.map(&:to_i)

batters = Hash.new(0)

n.times do |i|
  score = a[i]
  (i + 1).times do |ii|
    batters[ii] += score
  end
end

pp batters.values.count { |b| b >= 4 }
