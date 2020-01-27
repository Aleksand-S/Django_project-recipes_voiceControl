$(function () {


    // add field with ingredient
    var buttonAddIngredient = $('#add_field_ingredient');
    var fieldByTagP = $('p').eq(1);
    buttonAddIngredient.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        var newField = fieldByTagP.clone();
        $('p').eq(-1).after(newField);

    });


    // delete last field with ingredient
    var buttonDelIngredient = $('#del_field_ingredient');
    buttonDelIngredient.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        var fieldsByTagP = $('p');
        if (fieldsByTagP.length > 2) {
            fieldsByTagP.eq(-1).detach()
        }
    });


});