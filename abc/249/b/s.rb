s = gets

perfect = s =~ /[A-Z]/ && s =~ /[a-z]/ && s.size == s.split("").uniq.size

puts perfect ? "Yes" : "No"
