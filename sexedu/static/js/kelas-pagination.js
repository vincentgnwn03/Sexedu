$(document).ready(function() {
    let thisPage = 1;
    let limit = 6;
    let list = $('.card-course-list .card');

    function loadItem() {
        let beginGet = limit * (thisPage - 1);
        let endGet = limit * thisPage - 1;
        
        list.each(function(key, card) {
            if (key >= beginGet && key <= endGet) {
                $(card).css('display', 'block');
            } else {
                $(card).css('display', 'none');
            }
        });

        listPage();
    }

    loadItem();

    function listPage() {
        let count = Math.ceil(list.length / limit);
        const listPageContainer = $('.listPage');
        listPageContainer.empty();

        if (thisPage != 1) {
            let prev = $('<li>').text('Prev').css({
                color: '#9E9D9D',
                fontSize: '20px'
            }).on('click', function() {
                changePage(thisPage - 1);
            });
            listPageContainer.append(prev);
        }

        for (let i = 1; i <= count; i++) {
            let newPage = $('<li>').text(i);
            if (i === thisPage) {
                newPage.addClass('active');
            }
            newPage.on('click', function() {
                changePage(i);
            });
            listPageContainer.append(newPage);
        }

        if (thisPage != count) {
            let next = $('<li>').text('Next').css({
                color: '#9E9D9D',
                fontSize: '20px'
            }).on('click', function() {
                changePage(thisPage + 1);
            });
            listPageContainer.append(next);
        }
    }

    function changePage(i) {
        thisPage = i;
        loadItem();
    }
});
