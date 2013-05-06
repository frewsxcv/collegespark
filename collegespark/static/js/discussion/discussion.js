var Pagination = function(total) {
    this.total_rows = total;
    this.curr_page  = 1;
    this.per_page   = 3;
    this.page_count = this.set_page_count();
};

Pagination.prototype.has_next = function() {
    return this.curr_page + 1 <= this.page_count;
};

Pagination.prototype.has_prev = function() {
    return this.curr_page - 1 >= 1;
};

Pagination.prototype.is_valid_page = function(page_num) {
    console.log(this.page_count + "  " + page_num);
    return page_num >= 1 && page_num <= this.page_count;
};

Pagination.prototype.set_page_count = function() {
    var count = 0;

    if ((this.total_rows % this.per_page) !== 0)
        count = (this.total_rows / this.per_page) + 1;
    else
        count = (this.total_rows / this.per_page);

    return count;
};

var Category = function(categories_count) {
    Pagination.call(this, categories_count);
};

Category.prototype.__proto__ = Pagination.prototype;

Category.prototype.get_categories = function(page_num) {
    console.log(page_num);
    var url = window.location.pathname;
    var that = this;
    url += "category?page=" + page_num;
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

    $(".category-table > table > tbody").replaceWith(rows);
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