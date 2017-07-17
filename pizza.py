import pandas as pd

pizzas = [
    "Hawaiian",
    "Champagne Ham & Cheese",
    "Beef & Onion",
    "Pepperoni",
    "Simply Cheese",
    "Bacon & Mushroom",
    "Italiano",
    "The Deluxe",
    "Ham, Egg & Hollandaise",
    "Americano",
    "Mr Wedge",
    "BBQ Meatlovers"
    ]

df = pd.DataFrame(pizzas, columns=["Pizzas"])
df.loc[:8, "Prices"] = 7.50     # First 7 items.
df.loc[8:, "Prices"] = 13.50    # All the rest.
df.index += 1                   # So that it's not zero-indexed.
total_bill = 0.0                # Meh.

print "Welcome to Pizza Planet!" # So unoriginal, I know.
print
print "Here's our menu!"
print
# Following method taken and modified from unutbu's amazing answer
# here: http://stackoverflow.com/questions/25777037
print df.to_string(justify='left',
                   header=False,
                   formatters={
                    'Pizzas':'{{:<{}s}}'.format(
                        df['Pizzas'].str.len().max()
                        ).format,
                    'Prices':'     ${:.2f}'.format})
print
print "Input a number and press enter to select an item."
print "Input 'done' to finish your order and tabulate your bill."
print "Input 'exit' to cancel your orders."

while True:

    order = raw_input(">>>  ")

    if order == 'exit':
        break
    elif order == 'done':
        print "Your total bill is ${:.2f}.".format(total_bill)
        raw_input("Press any key to exit.")
        break
    elif int(order) in df.index:
        item = df.loc[int(order), "Pizzas"]     # Get the respective items
        price = df.loc[int(order), "Prices"]    # by indexing order input.
        print "You've selected {}! That would be ${:.2f}.".format(item, price)
        total_bill += price
        continue
    else:
        print "Don't be an idiot." # :-)
        raw_input("Press any key to exit.")
        break

             <div style="overflow: scroll; height:300px;" >
            {{sol.code|safe}}
             </div>

<!-- social share -->

    <meta property="og:type" content="article">
    <meta property="og:title" content="{{question.title}}">
    <meta property="og:description" content="{{question.summary}}">
    <meta property="og:url" content="/probandsols/problem/{{question.slug}}">
    <meta property="og:image" content="/media/{{solution.photo}}">



    <iframe src="http://www.zekestats.com/media/{{file}}" width="100%" height="1000">
    {{solution.code|safe}}
    </iframe>



                <iframe   src="http://www.zekestats.com/media/{{sol.datarcat}}"  width="100%" height="1000">
              {{sol.code|safe }}
               </iframe>
             </div>



             <div style="overflow: scroll; height:300px;" >

           <iframe src="http://www.zekestats.com/media/{{file}}" width="100%" height="1000">
           {{solution.code|safe}}
           </iframe>

             </div>
