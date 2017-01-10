import pprint
menu = {
  "1": { "Name":"Half-Dozen Eggs", "Price":1.09},
  "2": { "Name":"Yoplait Yogurt", "Price":1.19},
  "3": { "Name":"Miss Vickies Chips", "Price":1.25},
  "4": { "Name":"Del Monte Fruit Cup", "Price":2.09},
  "5": { "Name":"Minute Maid Juices", "Price":2.19},
  "6": { "Name":"Chex Mix", "Price":2.19},
  "7": { "Name":"Simply Juices", "Price":2.29},
  "8": { "Name":"Chobani Greek Yogurt", "Price":2.29},
  "9": { "Name":"Prairie Farms Milk Quart", "Price":2.29},
  "10": { "Name":"Twix Ice Cream Bar", "Price":2.29},
  "11": { "Name":"Snickers Ice Cream Bar", "Price":2.29},
  "12": { "Name":"Silk Soy Milk Quart", "Price":2.99},
  "13": { "Name":"Yogurt Parfait", "Price":2.99},
  "14": { "Name":"Chex Muddy Buddies", "Price":3.19},
  "15": { "Name":"Magnum Ice Cream", "Price":3.29},
  "16": { "Name":"Illy", "Price":3.35},
  "17": { "Name":"Sabra Hummus", "Price":3.39},
  "18": { "Name":"Soup", "Price":3.49},
  "19": { "Name":"Chips", "Price":3.49},
  "20": { "Name":"Odwalla Smoothie", "Price":3.69},
  "21": { "Name":"YUP Milk", "Price":3.79},
  "22": { "Name":"Core Power", "Price":3.79},
  "23": { "Name":"Cheese Pizza", "Price":5.25},
  "24": { "Name":"Savory Chicken Sandwich", "Price":5.49},
  "25": { "Name":"Chipotle Chicken Sandwich", "Price":5.49},
  "26": { "Name":"Chicken Caesar Sandwich", "Price":5.49},
  "27": { "Name":"Roast Beef & Provolone Sandwich", "Price":5.49},
  "28": { "Name":"Meatball Parmesan Sandwich", "Price":5.49},
  "29": { "Name":"Ham & Swiss Sandwich", "Price":5.49},
  "30": { "Name":"Turkey & Provolone Sandwich", "Price":5.49},
  "31": { "Name":"The Italian Sandwich", "Price":5.49},
  "32": { "Name":"Lisa's Tuna Salad Sandwich", "Price":5.49},
  "33": { "Name":"The Mediterranean Sandwich", "Price":5.49},
  "34": { "Name":"Mediterranean Hummus Wrap", "Price":5.49},
  "35": { "Name":"Chicken Caesar Wrap", "Price":5.49},
  "36": { "Name":"Vegetarian Pizza", "Price":5.75},
  "37": { "Name":"Ben & Jerry's Ice Cream Pint", "Price":5.99},
  "38": { "Name":"Buffalo Chicken Flatbread", "Price":6.00},
  "39": { "Name":"Chicken Caesar Flatbread", "Price":6.00},
  "40": { "Name":"Sushi", "Price":6.10},
  "41": { "Name":"Sausage Pizza", "Price":6.25},
  "42": { "Name":"Pepperoni Pizza", "Price":6.25},
  "43": { "Name":"Supreme Pizza", "Price":6.25},
  "44": { "Name":"Talenti Gelato", "Price":6.29},
  "45": { "Name":"Beef Jerky", "Price":6.99},
  "46": { "Name":"Sandwich Combo", "Price":7.58}
}

if type(next (iter (menu.values()))):
    pp = pprint.PrettyPrinter(indent=4)
    new_menu = {}
    for key in menu.keys():
        new_key = int(key)
        new_menu[new_key] = menu[key]
    pp.pprint(new_menu)
    menu = new_menu