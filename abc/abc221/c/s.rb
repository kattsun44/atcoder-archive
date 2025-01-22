n = gets.chomp
permutations = n.split("").permutation.uniq

ans = 0
permutations.each do |ps|
  p = ps.join
  n.length.times do |i|
    ans = [ans, p[0..i].to_i * p[i+1..n.length].to_i].max
  end
end
puts ans
