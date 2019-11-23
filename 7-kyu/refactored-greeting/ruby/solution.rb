class Person

  attr_reader :name

  def initialize(name)
    @name = name
  end
  
  def greet(person_name)
    "Hello #{person_name}, my name is #{@name}"
  end
    
end

