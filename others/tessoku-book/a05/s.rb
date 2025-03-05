n, k = gets.chomp.split.map(&:to_i)

count = 0

1.upto(n) do |a|
  1.upto(n) do |b|
    count += 1 if 1 <= k-a-b && k-a-b <= n
  end
end

puts count
