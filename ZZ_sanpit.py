# Next Steps
# Add currency formatting & Headings
# integrate this component with the base component
# Show students that they can use comments at the top of a component at the
# end of a period so that they know what they got and what they need to do next
# add this idea to the last discussion slide!

# PS: In base component remember to calculate surcharge once payment method has been chosen!!

import pandas

# dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()

# output table with ticket data
print(mini_movie_frame)

# output total ticket sales and profit
print("Total Ticket Sales: ${:.2f}".format(total))

