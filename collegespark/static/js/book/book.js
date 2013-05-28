$(".carousel-book").CloudCarousel(
    {
        xPos: 550,
        yPos: 10,
        buttonLeft: $("#left-but"),
        buttonRight: $("#right-but"),
        altBox: $("#alt-text"),
        titleBox: $("#title-text")
    }
);

var Book = function(book_count, per_page) {
    Pagination.call(this, book_count, 6);
};

Book.prototype = Object.create(Pagination.prototype);

Book.prototype.update_table = function(data) {
    console.log("*****book update********");
    var school_book_list = "<div class='school-book-list'>";
    var count = 0;
    var image_src;

    for (var key in data) {
        var fields = data[key].fields;
        var book_name = fields.book_name;
        if (count % 3 === 0) {
            school_book_list +=  "<ul class='thumbnails'>";
        }
        if (!fields.image) {
            image_src = "/static/img/noImage.jpg";
        }
        else {
            image_src = "/media/" + fields.image;
        }
        school_book_list += "<li class='span3'><div class='thumbnail'>" +
                            "<a class='plain' href=" + "/" +
                            get_school_name() + "/book/" +
                            data[key].pk + ">" +
                            "<div class='book-name-caption'>" +
                            "<span class='caption-detail'>" + fields.book_name +
                            "</span></div>" +
                            "<img src= '" + image_src + "' " +
                            "alt='' style='height:250px;width:100%;'>" +
                            "<div class='book-price-caption'>" +
                            "<span class='caption-detail'>" + "$" + fields.price +
                            "</span></div>" +
                            "</a></div></li>";
        if (((count+3) %3 === 0) || ((count+2) %3 === 0)) {
            school_book_list += "<li class='span1'></li>";
        }
        else if ((count+1) %3 === 0) {
            school_book_list += '</ul>';
        }
        ++count;
    }
    console.log("js book count " + count);

    school_book_list += "</div>";

    $(".school-book-list").replaceWith(school_book_list);

};

Book.prototype.set_book_pagination = function() {
    pagination = this.get_pagination_num_html();

    $(".book-pagination ul").replaceWith(pagination);
};

function change_page(obj, $this) {
    var page = $this.text().trim();
    var next_page;
    var extra_context = {};

    console.log("Page is " + page);
    next_page = obj.get_next_page(page);
    obj.get_page_data("book", next_page, extra_context, obj.update_table);
}
