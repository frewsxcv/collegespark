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