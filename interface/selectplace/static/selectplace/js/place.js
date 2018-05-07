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
            data_to_render = data;
            clear_all_flates();
            render_new_flats();
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


var data_to_render = [{'area': null, 'currency': 'UAH', 'district': 'Dnipr', 'id': 3, 'name': 'text', 'price': 12.94, 'url': null, 'weight':
    0.8230043810998888}, {'area': null, 'currency': 'UAH', 'district': 'Dnipr', 'id': 2, 'name': 'text', 'price': 120.94,
    'url': null, 'weight': 0.08805752184085135}, {'area': null, 'currency': 'UAH', 'district': 'Dnipr', 'id': 5, 'name':
    'text', 'price': 120.94, 'url': null, 'weight': 0.08805752184085135}, {'area': null, 'currency': 'UAH', 'district':
    'Dnipr', 'id': 108, 'name': 'text', 'price': 12094.0, 'url': null, 'weight': 0.0008805752184085135}];

function render_new_flats() {
    var optimalFlats = d.getElementById('optimal-flats');
    var data_to_renderslen = data_to_render.length;
    for(var i = 0; i < data_to_renderslen; i++){
        console.log(data_to_render[i].url);
       /* optimalFlats.innerHTML += '<li class="one-flat"><span>Street: '+data_to_render[i].name+'.\<' +
            '/span><p>Price:'+data_to_render[i].price+'<span> '+data_to_render[i].currency+'</span></p><span><a href="'+data_to_render[i].url+'">More</a>\<' +
            '/span> </li>';*/
       if (data_to_render[i].src) {
           var src_img = '';
       }
        optimalFlats.innerHTML +='<li class="one-flat">\n' +
        '                <div class="one-flat-description">\n' +
        '                    <p>Street: '+data_to_render[i].name+'</p>\n' +
        '                    <p>District: '+data_to_render[i].district+'</p>\n' +
        '                    <p>Price:'+data_to_render[i].price+'<span> '+data_to_render[i].currency+'</span></p>\n' +
        '                    <p>Area: '+data_to_render[i].area+' м²</p>\n' +
        '                    <p><a target="_blank" href="'+data_to_render[i].url+'">More</a></p>\n' +
        '                </div>\n' +
        '            </li>';
    }
}

function clear_all_flates() {
    var optimalFlats = d.getElementById('optimal-flats');
    while (optimalFlats.firstChild) {
        optimalFlats.removeChild(optimalFlats.firstChild);
    }
}
$('#clean').click(clear_all_flates);

/*render_new_flats();*/

/*clear_all_flates();*/
/*var TEST_DATA_TO_RENDER = {
    has_next: false,
    has_prev: false,
    data: [{area:"Kiev", currency: "UAH", district: "Dnipr", id: "2", name: "Pechersk", price: "120.94", url: "None"},
        {area:"Kiev", currency: "UAH", district: "Dnipr", id: "3", name: "Schevchenko", price: "120.94", url: "None"}
    ]
}*/