s = gets.chomp.split("")

h = {
  "()" => 0,
  "[]" => 0,
  "<>"=> 0,
}

latest = []

def exec(s, h, latest)
  colorful = true
  s.each do |c|
    if c == "("
      h["()"] += 1
      latest << c
    elsif c == ")"
      if latest[-1] != "("
        colorful = false
      else
        h["()"] -= 1
        latest = latest[0...latest.size-1]
      end
    elsif c == "["
      h["[]"] += 1
      latest << c
    elsif c == "]"
      if latest[-1] != "["
        colorful = false
      else
        h["[]"] -= 1
        latest = latest[0...latest.size-1]
      end
    elsif c == "<"
      h["<>"] += 1
      latest << c
    elsif c == ">"
      if latest[-1] != "<"
        colorful = false
      else
        h["<>"] -= 1
        latest = latest[0...latest.size-1]
      end
    end

    if h.values.any? { _1 == -1 }
      puts "No"
    end
  end

  colorful && h.values.all? { _1 == 0 }
end

puts exec(s, h, latest) ? "Yes" : "No"
