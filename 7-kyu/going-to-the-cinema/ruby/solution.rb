def movie(card, ticket, perc)
  count = 1
  count += 1 until price_systemB(card, ticket, perc, count).ceil <
                   price_systemA(ticket, count)
  count - 1
end

def price_systemA(ticket, times)
  ticket * times
end

def price_systemB(card, ticket, perc, times)
  card + ticket * (1.0 - perc**times)/(1.0 - perc)
end
