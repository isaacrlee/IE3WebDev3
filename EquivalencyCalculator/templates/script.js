var menu = {{ menu | safe }}; //get menu in json form from python file
$(function () {
    var total = 0; //variable holding value of items in cart
    $('#meal a').click(function () {
        var meal;
        $('#meal a').removeClass('bg-yellow');
        $(this).addClass('bg-yellow');
        id = $(this).attr('id'); //get id of meal that has been clicked
        if (id == "b") meal = 5.00;
        else if (id == "l") meal = 7.00;
        else if (id == "d") meal = 9.00;
        $('#meal-val').text(meal); //update meal value text
    });
    $('#menu a').click(function () { //handler for when a menu item is clicked (added to cart)
        id = parseInt($(this).attr('id')); //get id of item that has been clicked (to allow price lookup)
        var val = menu[id]['Price']; //get price of item from id and menu
        total += val; //add price to cart total
        total = Math.round(total * 100) / 100; //rounds total to 2 decimal places
        $('#cart-value').text(total.toFixed(2)); //update cart text toFixed makes 2 decimal places always shown
        text = '<li>' + menu[id]['Name'] + ": " + val.toFixed(2) /*+ '<a href=\'#\' id=\'remove\'> REMOVE</a>'*/ + '</li>';
        $('#cart-items').append(text);
    });
    $('#reset').click(function () { // handler for when reset is clicked (cart is cleared)
        total = 0; //reset cart total to 0
        $('#cart-items').empty(); //empties cart
        $('#cart-value').text(total); //update cart text
    });
    // $('a#remove').click(function () {
    //     console.log("remove attempted");
    //     $(this).parent().remove();
    // });
});