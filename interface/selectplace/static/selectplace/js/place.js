console.log(this_url);
d = document;
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

var info =  {
                houses:[{name: "house1", price: 100, len_to_metro: 3000},
                    {name: "house2", price: 60, len_to_metro: 5000}],
                cri: [{name: "price", priority: 4}, {name: "len_to_metro", priority: 6}]
            };
console.log(csrftoken);


$("#send-data").click(
    function () {
        var filters = getFilters();
        var criterias = [{name: "price", priority: 4}, ]
        var info = {filters: filters, cri: criterias}
        console.log(info);
        var request = $.ajax({
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrftoken
            },
            url: this_url,
            data: JSON.stringify(info)
            });

        console.log(request);
        request.done(function (data) {
            console.log(data);
            console.log();
        });
    }
)

function getFilters() {
    var district = d.getElementsByName('district')[0].value;
    var name = d.getElementsByName('street')[0].value;
    var currency_field = d.getElementsByName('currency')[0];
    var currency = currency_field.options[currency_field.selectedIndex].value;
    var price_gte = d.getElementsByName('min_price')[0].value;
    var price_lte = d.getElementsByName('max_price')[0].value;
    return {
        district: district, name: name, currency: currency, price_lte: price_lte, price_gte: price_gte
    }
}

var TEST_DATA_TO_RENDER = {
    has_next: false,
    has_prev: false,
    data: [{area:"Kiev", currency: "UAH", district: "Dnipr", id: "2", name: "Pechersk", price: "120.94", url: "None"},
        {area:"Kiev", currency: "UAH", district: "Dnipr", id: "3", name: "Schevchenko", price: "120.94", url: "None"}
    ]
}

function render_new_flats() {

}

