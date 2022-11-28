$(function() {
    $("#fcomp").autocomplete({
        source: "/autocomplete",
        minLength: 2,
        select: function(event, ui) {
            console.log(ui.item.value); // not in your question, but might help later
        }
    });
})