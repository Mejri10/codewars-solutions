class TvRemoteKeyboard

  @@KEYBOARD = [
    %W(a b c d e 1 2 3),
    %W(f g h i j 4 5 6),
    %W(k l m n o 7 8 9),
    %W(p q r s t . @ 0),
    %W(u v w x y z _ /),
    ["SHIFT", " ", "", "", "", "", "", "",]
  ]
  
  def initialize(start='a')
    @start = start
  end

  def number_of_clicks(word)
    keys = [@start] + word.chars
    clicks = 0
    current_case = get_case(@start)

    keys.each_cons(2) do |key1, key2|
      next_key_case = get_case(key2)
      if next_key_case.nil? || current_case == next_key_case
        clicks += distance_between_keys(key1.downcase, key2.downcase) + 1
      else
        d1 = distance_between_keys(key1.downcase, "SHIFT") + 1
        d2 = distance_between_keys("SHIFT", key2.downcase) + 1
        clicks += (d1 + d2)
        current_case = next_key_case
      end
    end
    clicks
  end

  private

  def get_case(c)
    case c
    when /[a-z]/ then 'lower'
    when /[A-Z]/ then 'upper'
    else nil
    end
  end
  
  def key_position(key)
    @@KEYBOARD.each_with_index do |row, i|
      row.each_with_index do |col, j|
        return [i, j] if col == key
      end
    end
  end

  def distance_between_keys(key1, key2)
    position_key1 = key_position(key1)
    position_key2 = key_position(key2)

    position_key1
      .zip(position_key2)
      .reduce(0){ |sum, (pos1, pos2)| sum + (pos1 - pos2).abs }
  end
  
end 

def tv_remote(words)
  TvRemoteKeyboard.new.number_of_clicks(words)
end