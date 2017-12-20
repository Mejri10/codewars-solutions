def pizza_rewards(customers, min_orders, min_price): 
    return [customer for customer in customers if len([order for order in customers[customer] if order >= min_price]) >= min_orders]