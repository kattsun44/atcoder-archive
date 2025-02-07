az = [*"a".."z"]
s, t = 2.times.map { gets.chomp.split("").map { |c| az.index(c) } }

puts t.zip(s).map { |t, s| (t - s) % 26 }.uniq.size == 1 ? "Yes" : "No"
