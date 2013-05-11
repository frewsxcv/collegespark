var Category = function(categories_count, per_page) {
    Pagination.call(this, categories_count, per_page);
};

Category.prototype = Object.create(Pagination.prototype);

Category.prototype.get_categories = function(page_num) {
    console.log(page_num);
    var url = window.location.pathname;
    var that = this;
    url += "category?page=" + page_num + "&per_page=" + this.per_page;
    $.get(url,  function(data){
        console.log(data);
        that.update_table(data);
    });
};

Category.prototype.update_table = function(data) {
    console.log("*************");
    var rows = "<tbody>";
    var count = 0;

    for (var key in data) {
        var fields = data[key].fields;
        var name = fields.name;
        var topic_count = fields.topic_count;

        rows += "<tr>\n" +
                "\t<td>" + 0 + "</td>\n" +
                "\t<td>" + name + "</td>\n" +
                "\t<td>" + topic_count + "</td>\n" +
                "</tr>\n";
        ++count;
    }
    rows += "</tbody>";

    $(".category-table > tbody").replaceWith(rows);
};

Category.prototype.set_category_pagination = function() {
    var pagination = "";
    console.log(this.page_count);
    pagination += "<ul>\n<li><a>Prev</a></li>\n";

    for (var i = 1; i <= this.page_count; ++i) {
        pagination += "\t<li><a>" + i + "</a></li>\n";
    }
    pagination += "\t<li><a>Next</a></li>\n</ul>\n";

    $(".category-pagination ul").replaceWith(pagination);
};

Category.prototype.get_page = function(page) {
    if (!isNaN(page)) {
       var page_num = parseInt(page, 10);

       if (this.is_valid_page(page_num) &&
          page_num !== this.curr_page) {
          this.get_categories(page_num);
          this.curr_page = page_num;

       } else if (page_num !== this.curr_page) {
          this.get_categories(this.page_count);
          this.curr_page = this.page_count;
       }

    } else {
       console.log("-----------");
       if (page === "Prev" && this.has_prev()) {
          this.curr_page -= 1;
          this.get_categories(this.curr_page);
       } else if (page === "Next" && this.has_next()) {
          this.curr_page += 1;
          this.get_categories(this.curr_page);
       }
    }
};