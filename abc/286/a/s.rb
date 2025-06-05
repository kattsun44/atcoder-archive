N, P, Q, R, S = gets.chomp.split.map { _1.to_i - 1 }
a = gets.chomp.split.map(&:to_i)

puts (a[0...P] + a[R..S] + a[Q + 1...R] + a[P..Q] + a[S + 1..]).join(" ")
