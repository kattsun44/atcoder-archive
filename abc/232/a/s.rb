puts gets.chomp.split("x").map(&:to_i).inject(:*)
