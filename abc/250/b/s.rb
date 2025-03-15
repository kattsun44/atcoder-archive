n, a, b = gets.chomp.split.map(&:to_i)

n.times do |i|
  a.times do
    n.times do |j|
      is_white = ((i + j) % 2 == 0) ? true : false
      if is_white
        print "." * b
        is_white = false
      else
        print "#" * b
        is_white = true
      end
    end
    puts ""
  end
end
