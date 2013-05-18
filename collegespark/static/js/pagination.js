/*
 * Before editing this file talk to hormoz. Just inherit from Pagination
 * and use it. Look at /static/js/discussion/discussion.js for example.
 */

var Pagination = function(total_rows, per_page) {
    this.total_rows = total_rows;
    this.curr_page  = 1;
    this.per_page   = typeof per_page === 'undefined' ? 4 : per_page;
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

Pagination.prototype.get_pagination_num_html = function() {
    var pagination = "";
    console.log(this.page_count);
    pagination += "<ul>\n<li><a>Prev</a></li>\n";

    for (var i = 1; i <= this.page_count; ++i) {
        pagination += "\t<li><a>" + i + "</a></li>\n";
    }
    pagination += "\t<li><a>Next</a></li>\n</ul>\n";

    return pagination;
};

Pagination.prototype.get_next_page = function(page) {
    if (!isNaN(page)) {
       var page_num = parseInt(page, 10);

       if (this.is_valid_page(page_num) &&
          page_num !== this.curr_page) {
          this.curr_page = page_num;

       } else if (page_num !== this.curr_page) {
          this.curr_page = this.page_count;
       }

    } else {
       console.log("-----------");
       if (page === "Prev" && this.has_prev()) {
          this.curr_page -= 1;
       } else if (page === "Next" && this.has_next()) {
          this.curr_page += 1;
       }
    }

    return this.curr_page;
};

Pagination.prototype.get_page_data = function(page_name, page_num, extra_context, callback) {
    console.log(page_num);
    var url = window.location.pathname;

    console.log(extra_context);
    url += "/paginator/" + page_name + "?page=" + page_num + "&per_page=" + this.per_page;
    for (var key in extra_context)
        if (extra_context.hasOwnProperty(key))
            url += "&" + key + "=" + extra_context[key];

    $.get(url,  function(data){
        console.log(data);
        callback(data);
    });
};