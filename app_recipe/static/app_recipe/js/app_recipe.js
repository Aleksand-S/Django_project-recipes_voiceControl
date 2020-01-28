$(function () {

    // add field with ingredient/quantity/unit
    let buttonAddIngredient = $('#add_field_ingredient');
    let ingredientsBlock = $('.ingredients_block');
    buttonAddIngredient.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        let newElement = ingredientsBlock.children().eq(0).clone();
        ingredientsBlock.append(newElement);

    });

    // delete last field with ingredient/quantity/unit
    let buttonDelIngredient = $('#del_field_ingredient');
    buttonDelIngredient.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        let ingredientsBlock = $('.ingredients_block');
        if (ingredientsBlock.children().length > 1) {
            ingredientsBlock.children().eq(-1).detach()
        }
    });


});