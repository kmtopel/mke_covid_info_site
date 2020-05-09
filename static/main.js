var submit_btn = document.getElementById('post-submit-btn');
var filter_btn = document.getElementById('filter-results');
var posts = document.getElementsByTagName('article');

function filter_results()
    {
    var choices = document.getElementById("post_type_filter");
    var selected_option = choices.options[choices.selectedIndex].value;
    for (var i=0; i<posts.length; i++)
        {
        if (selected_option == "Show All")
            {
                posts[i].style.visibility = 'visible';
            }
        else if (posts[i].className != selected_option)
            {
                posts[i].style.visibility = 'hidden';
            }
        else
            {
                document.getElementsByClassName(selected_option).style.display == 'visible';
            }
        }
    }