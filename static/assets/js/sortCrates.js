function sortCrates(attribute, numeric, ascending) {
    var section = $("#crates-section .card-grid");
    var cards = section.children(".card");

    var default_value = numeric ? 0 : "";

    cards.sort(function (a, b) {
        var aAttr = a.getAttribute(attribute) || default_value;
        var bAttr = b.getAttribute(attribute) || default_value;

        if (numeric) {
            aAttr = parseInt(aAttr);
            bAttr = parseInt(bAttr);
        } else {
            aAttr = aAttr.toUpperCase();
            bAttr = bAttr.toUpperCase();
        }

        if (aAttr > bAttr) {
            return ascending ? 1 : -1;
        } else if (aAttr < bAttr) {
            return ascending ? -1 : 1;
        } else {
            return 0;
        }
    });

    cards.detach().appendTo(section);
}

$(document).ready(function () {
    var sortDropdown = $("#sort-menu");

    sortDropdown.dropdown({
        onChange: function (value) {
            let [field, modifier] = value.split("_");

            sortCrates(field, modifier == "num", modifier == "asc");

            localStorage.setItem("sortPreference", value);
        },
    });

    var sortPreference = localStorage.getItem("sortPreference");
    if (sortPreference) {
        sortDropdown.dropdown("set selected", sortPreference);
    }
});
