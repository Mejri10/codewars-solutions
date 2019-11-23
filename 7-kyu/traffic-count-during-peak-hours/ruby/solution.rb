def traffic_count(arr)
  (4...8).zip(arr.each_slice(6)).map{|hour, values| ["#{hour}:00pm", values.max]}
end