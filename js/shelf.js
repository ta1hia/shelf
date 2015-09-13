Util = {
    fire: function(func, funcname, args) {
        var namespace = BookShelf; // indicate your obj literal namespace here

        funcname = (funcname === undefined) ? 'init' : funcname;
        if (func !== '' && namespace[func] && typeof namespace[func][funcname] == 'function') {
            namespace[func][funcname](args);
        }
    },
    loadEvents: function() {
        var bodyId = document.body.id;
        Util.fire('common');
        $.each(document.body.className.split(/\s+/), function(i, classnm) {
            Util.fire(classnm);
            Util.fire(classnm, bodyId);
        });
        Util.fire('common', 'finalize');
    },
    isNullOrEmpty: function(obj) {
        return (obj == null || obj == "");
    },
};


BookShelf = {
    common: {
        init: function() {
        },
        finalize: function() {
            }
    },
    front: {
        init: function() {
            BookShelf.front.createAllShelves()
            },
        createAllShelves: function() {
            shelves = JSON.parse(data)
            for (i = 0; i < shelves.length; i++) {
                text = ""
                books = shelves[i].books
                for (j = 0; j < shelves[i].total; j++) {
                    if (typeof books[j] != 'undefined') {
                        text += "<div class='book'><span class='book_title'>" + books[j].title + "</span>, <span class='book_author'>" + books[j].author + "</span></div>"
                    }
                }
                document.getElementById(shelves[i].name).innerHTML = text
            }
        },
    },
};

ShelfManager = {
    reading: null,
    read: null,
    toread: null,
    getReading: function() {
        // https://www.goodreads.com/review/list.xml?v=2&key=vxZe7MkoUbQOmzF71sryw&shelf=read&id=4933497-tahia
    }

}

$(document).ready(Util.loadEvents);
