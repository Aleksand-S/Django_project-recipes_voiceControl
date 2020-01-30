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


    // add field with step/image
    let buttonAddStep = $('#add_next_step');
    let stepsBlock = $('.steps_block');
    buttonAddStep.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        let newStepElement = stepsBlock.children().eq(0).clone();

        // last step number +1
        let innerTextLastElement = $('.steps_block').children().eq(-1).children().eq(0);
        let textInElement = innerTextLastElement.text().split(' ')[1];
        textInElement ++;
        innerTextForAddToElement = 'Krok ' + textInElement;

        // add element with text 'Step <number>'
        newStepElement.children().eq(0).text(innerTextForAddToElement);
        stepsBlock.append(newStepElement);
    });


    // delete last field with step/image
    let buttonDelStep = $('#del_prev_step');
    buttonDelStep.on('click', function (event) {
        event.preventDefault();  // blocks the POST method on currently button
        let stepBlocks = $('.steps_block').children();
        if (stepBlocks.length > 1) {
            stepBlocks.eq(-1).detach()
        }
    });


});