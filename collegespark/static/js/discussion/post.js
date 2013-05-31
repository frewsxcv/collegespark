var Post = function(post_count, per_page) {
    Pagination.call(this, post_count, per_page);
};

Post.prototype = Object.create(Pagination.prototype);

Post.prototype.update_table = function(data) {
    console.log("*************");
    var rows = "<tbody class='table-list'>";
    var count = 0;
    var school_name = get_school_name();

    console.log(data);
    for (var key in data) {
        var fields = data[key].fields;
        console.log(fields);
        var name = fields.post_topic;
        var post_count = fields.post_count;
        rows += "<tr class='table-row' " +
                "data-href='/" + school_name + "/discussion/" + data[key].pk + "' >" +
                "\t<td>" + count + "</td>\n" +
                "\t<td class='post-name'>" + name + "</td>\n" +
                "\t<td>" + post_count + "</td>\n" +
                "</tr>\n";
        ++count;
    }

    rows += "</tbody>";

    $(".post-table > tbody").replaceWith(rows);

    $(".table-list > tr").click(function() {
       redirect_to_post($(this));
    });
};

Post.prototype.set_post_pagination = function() {
    pagination = this.get_pagination_num_html();

    $(".table-pagination ul").replaceWith(pagination);
};

function change_page(obj, extra_context, $this) {
    var page = $this.text().trim();
    var next_page;

    console.log("Page is " + page);
    next_page = obj.get_next_page(page);
    obj.get_page_data("post", next_page, extra_context, obj.update_table);
}

function redirect_to_post($this) {
    var post_name = $this.find(".post-name").text().trim();
    var url = $this.data("href");

    post_name = post_name.replace(/\s+/g, '-');
    url += "/" + post_name;
    window.location = url;
}