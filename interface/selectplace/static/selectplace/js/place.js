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
        console.log("Yeyy");
        $.ajax({
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                "X-CSRFToken": csrftoken
            },
            url: this_url,
            data: JSON.stringify(info)
            });
    }
)

