s, _k = gets.chomp.split(" ")
k = _k.to_i

puts s.split("").permutation.sort.uniq[k-1].join
