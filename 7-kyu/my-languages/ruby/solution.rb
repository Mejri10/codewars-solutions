def my_languages(results)
  results.select{|k, v| v >= 60}.sort_by{|k, v| -v}.map{|k, v| k}
end