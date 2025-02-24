n, x = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
count = a.map { |k| [k, 0] }.to_h
count[x] = 1

loop do
  break if count[a[x-1]] >= 1
  count[a[x-1]] += 1
  x = a[x-1]
end

pp count.values.sum
