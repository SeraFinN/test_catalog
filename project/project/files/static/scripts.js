var shuffle = function (elements) {
    var items = elements;
    var rand_items = elements.clone();

    rand_items.sort(function () {
        return Math.random() - 0.5
    });

    items.each(function (index) {
        items.eq(index).replaceWith(rand_items.eq(index));
    });
};
