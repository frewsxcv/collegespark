var Category = function(category_count, per_page) {
    Pagination.call(this, category_count, per_page);
};

Category.prototype = Object.create(Pagination.prototype);

Category.prototype.update_table = function(data) {
    console.log("*************");
    var rows = "<tbody class='category-list'>";
    var count = 0;

    for (var key in data) {
        var fields = data[key].fields;
        var name = fields.name;
        var topic_count = fields.topic_count;
        rows += "<tr class='category-row'>\n" +
                "\t<td>" + 0 + "</td>\n" +
                "\t<td class='category-name'>" + name + "</td>\n" +
                "\t<td>" + topic_count + "</td>\n" +
                "</tr>\n";
        ++count;
    }

    rows += "</tbody>";

    $(".category-table > tbody").replaceWith(rows);

    $(".category-list > tr").click(function() {
       redirect_to_topic($(this));
    });
};

Category.prototype.set_category_pagination = function() {
    pagination = this.get_pagination_num_html();

    $(".category-pagination ul").replaceWith(pagination);
};

function change_page(obj, $this) {
    var page = $this.text().trim();
    var next_page;
    var extra_context = {};

    console.log("Page is " + page);
    next_page = obj.get_next_page(page);
    obj.get_page_data("category", next_page, extra_context, obj.update_table);
}

function redirect_to_topic($this) {
    var category_name = $this.find(".category-name").text().trim();
    var school_name = get_school_name();
    var url = "";

    category_name = category_name.replace(/\s+/g, '-');

    url += "/" + school_name + "/discussion/" + category_name;
    window.location = url;
}