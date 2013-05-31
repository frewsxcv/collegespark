var Topic = function(topics_count, per_page) {
    Pagination.call(this, topics_count, per_page);
};

Topic.prototype = Object.create(Pagination.prototype);

Topic.prototype.update_table = function(data) {
    console.log("*************");
    var rows = "<tbody class='table-list'>";
    var count = 0;

    console.log(data);
    for (var key in data) {
        var fields = data[key].fields;
        var name = fields.name;
        var post_count = fields.post_count;
        rows += "<tr class='table-row'>\n" +
                "\t<td>" + count + "</td>\n" +
                "\t<td class='topic-name'>" + name + "</td>\n" +
                "\t<td>" + post_count + "</td>\n" +
                "</tr>\n";
        ++count;
    }

    rows += "</tbody>";

    $(".topic-table > tbody").replaceWith(rows);

    $(".table-list > tr").click(function() {
       redirect_to_post($(this));
    });
};

Topic.prototype.set_topic_pagination = function() {
    pagination = this.get_pagination_num_html();

    $(".table-pagination ul").replaceWith(pagination);
};

function change_page(obj, extra_context, $this) {
    var page = $this.text().trim();
    var next_page;

    console.log("Page is " + page);
    next_page = obj.get_next_page(page);
    obj.get_page_data("topic", next_page, extra_context, obj.update_table);
}

function redirect_to_post($this) {
    var topic_name = $this.find(".topic-name").text().trim();
    var url = window.location.pathname;

    topic_name = topic_name.replace(/\s+/g, '-');
    url += "/" + topic_name;
    window.location = url;
}