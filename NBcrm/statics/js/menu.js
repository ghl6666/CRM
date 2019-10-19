$('.item .title').click(function () {

    $(this).nextAll().toggleClass('hide');
    $(this).parent().siblings().children('.body').addClass('hide')

})

// $('.item .title').click(function () {
//     $(this).next().toggleClass('hide');
//     console.log($(this).classList);
//     console.log($(this).next().classList);
//     $(this).parent().siblings().children('.body').addClass('hide')
//
// });

