n = gets.to_i
a = gets.chomp.split.map(&:to_i)
q = gets.to_i
lr = q.times.map { gets.chomp.split(" ").map(&:to_i) }
win, lose = 0, 0
prefix_sums = [0] + n.times.map { a[_1] == 1 ? win += 1 : lose += 1; [win, lose] }

q.times do |i|
  l, r = lr[i][0], lr[i][1]
  w = prefix_sums[r][0] - prefix_sums[l-1][0]
  l = prefix_sums[r][1] - prefix_sums[l-1][1]
  if w > l
    puts "win"
  elsif w == l
    puts "draw"
  else
    puts "lose"
  end
end
